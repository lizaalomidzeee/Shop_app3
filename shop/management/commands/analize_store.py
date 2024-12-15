from django.core.management import BaseCommand
from shop.models import Item, Tag, Category
from django.db.models import Count, Min, Max, Avg, Sum

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        items = Item.objects.select_related('category')
        for item in items:
            print(f"Item: {item.name}, Category: {item.category.name}")
        
        
        
        
        items = Item.objects.prefetch_related('tags')
        for item in items:
            tags = Item.tags.all()
            tag_names = [tag.name for tag in tags]
            print(f"Item: {item.name}, Tag: {','.join(tag_names)}")

            
        
        
        
        price_info = Item.objects.aggregate(
            max_price = Max('price'),
            min_price = Min('price'),
            avg_price = Avg('price')
        )
        print(f"Max price: {price_info['max_price']}")
        print(f"Min price: {price_info['min_price']}")
        print(f"Avg price: {price_info['avg_price']}")
        
        
        
        
        category = Category.objects.first()
        category_item_count = category.items.aggregate(total_items=Count('id'))
        print(f"Category '{category.name}' has {category_item_count['total_items']} items")

        
        

        categories = Category.objects.annotate(
            items_count = Count('items'),
            items_price_sum = Sum('items__price', default=0)
        ) 
        
        for category in categories:
            print(f'Category: {category.name}')
            print(f'Total items: {category.items_count}')
            print(f'Total price: {category.items_price_sum}')
        
        
        

        
        
        
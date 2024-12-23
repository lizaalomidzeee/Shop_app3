from django.db import models
from django.db.models import Count



class CategoryManager(models.Manager):
    def with_item_count(self):
        return self.annotate(item_count=Count("item"))
    
    
class ItemManager(models.Manager):
    def with_tag_count(self):
        return self.annotate(tag_count=Count("tags"))
    
    
class TagManager(models.Manager):
    def popular_tags(self, min_items):
        return self.annotate(item_count=Count("item")).filter(item_count__gte=min_items)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tags')
    
    objects = TagManager()
    
    def __str__(self):
        return self.name
    
    


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    objects = ItemManager()

    def __str__(self):
        return self.name
    


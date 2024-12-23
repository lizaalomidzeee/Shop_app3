from django.contrib import admin
from shop.models import Category, Item, Tag

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    
class TagInline(admin.StackedInline): 
    model = Item.tags.through
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [ItemInline]
    
admin.site.register(Category, CategoryAdmin)
    
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    search_fields = ('name', 'description')
    ordering = ('-price',)
    inlines = [TagInline]
    
admin.site.register(Item, ItemAdmin)
    
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Tag, TagAdmin)

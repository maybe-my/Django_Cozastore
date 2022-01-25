from django.contrib import admin
from .models import Product, Category


# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

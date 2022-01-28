from django.contrib import admin
from .models import Product, Category, News


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['email']



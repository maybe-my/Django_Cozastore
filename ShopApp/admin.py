from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, News
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


# @admin.register(Product)
# class ProductsAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'available', 'created']
#     list_filter = ['available', 'created', 'updated']
#     # list_editable = ['price', 'available']
#     prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['email']


class ProductsResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product


@admin.register(Product)
class ProductsResource(ImportExportActionModelAdmin):
    resource_class = ProductsResource
    list_display = ['name', 'image_show', 'price', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Image"
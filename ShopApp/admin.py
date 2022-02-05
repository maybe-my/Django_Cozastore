from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, News
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ProductsResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product


@admin.register(Product)
class ProductsResource(ImportExportActionModelAdmin):
    resource_class = ProductsResource
    list_display = ['id', 'tovar_name', 'image_show', 'price', 'category', 'available', 'created']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    def tovar_name(self, obj):
        if obj.name:
            return mark_safe("<a href='{0}' style='color: white'>{1}</a>".format(obj.id, obj.name))
        else:
            return "hi"

    image_show.__name__ = "Image"
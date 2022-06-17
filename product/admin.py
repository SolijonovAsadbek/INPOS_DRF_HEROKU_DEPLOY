from django.contrib import admin

# Register your models here.
from product.models import Product, Category


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class ProductInline(admin.StackedInline):
    model = Product
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated']
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date_created', 'date_updated']


# admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

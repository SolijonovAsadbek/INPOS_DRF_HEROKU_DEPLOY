from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    # product = ProductSerializer()

    class Meta:
        model = Category
        fields = ['title', 'description', 'product']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'category', 'bar_code', 'name', 'price', 'stock', 'available', 'image', 'description',
                  'updated_at']

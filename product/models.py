from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    product = models.ForeignKey('product.Product', blank=True, null=True, related_name='product',
                                on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Product(models.Model):
    category = models.ForeignKey('product.Category', null=False, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=120, null=False)
    price = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1000000000)])
    stock = models.PositiveIntegerField()
    # stock = models.BigIntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=600, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']

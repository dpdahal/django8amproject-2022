from django.db import models
from ckeditor.fields import RichTextField


class Settings(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicon/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Setting'

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banner/')
    description = RichTextField()

    class Meta:
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.title

    def get_limit_description(self):
        return self.description[:100]


class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product/')
    description = RichTextField()
    stock = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.product_name

    def get_limit_description(self):
        return self.description[:100]

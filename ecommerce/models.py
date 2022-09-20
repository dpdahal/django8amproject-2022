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

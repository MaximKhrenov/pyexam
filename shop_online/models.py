from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    title_category = models.CharField(max_length=400, primary_key=True)

    def __str__(self):
        return self.title_category


class Product(models.Model):
    title_product = models.CharField(max_length=150, unique=True)
    discription_product = models.CharField(max_length=500)
    price_product = models.IntegerField()
    count_products = models.IntegerField()
    cat = models.ForeignKey(Category)

    create_pr = models.DateTimeField(auto_now_add=True)
    update_pr = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_product

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


class Cart(models.Model):
    user = models.ForeignKey('auth.User')
    count_products = models.IntegerField()
    price_product = models.IntegerField()
    title = models.ForeignKey(Product, to_field='title_product', )


class Order(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    title = models.ForeignKey(Cart)

    def __str__(self):
        return self.title

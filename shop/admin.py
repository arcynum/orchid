from django import forms
from django.contrib import admin

from .models import Category, Product, Profile, Order, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Cart)
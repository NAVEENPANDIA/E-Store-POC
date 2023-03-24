from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.offer import Offer

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','offer','category']
    ordering = ['category']

class CustomerData(admin.ModelAdmin):
    list_display = ['username','mobile','email']

class OfferData(admin.ModelAdmin):
    ordering = ['Discount']

admin.site.register(Product , AdminProduct)
admin.site.register(Category)
admin.site.register(Offer,OfferData)
admin.site.register(Customer, CustomerData)

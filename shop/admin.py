from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Customer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


# Define the admin options for the Customer table
class CustomerList(admin.ModelAdmin):
    list_display = ('cust_id', 'cust_fname', 'phone')
    list_filter = ('cust_id', 'cust_fname')
    search_fields = ('cust_id', 'cust_fname',)
    ordering = ['cust_id', 'cust_fname']


admin.site.register(Customer, CustomerList)


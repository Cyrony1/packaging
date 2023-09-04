from django.contrib import admin
from . import models
from .models import Customer, Sample, Contact, Product, Invoice, Contact
# Register your models here.


class ContactInline(admin.TabularInline):
    model = models.Contact
    extra = 0


class CustomerProductInline(admin.TabularInline):
    model = models.Product
    extra = 0


class CustomerOrderInline(admin.TabularInline):
    model = models.Order
    extra= 0

class CustomerSampleInline(admin.TabularInline):
    model = models.Sample
    extra = 0


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerOrderInline, ContactInline, CustomerProductInline, CustomerSampleInline]
    list_display = ['title', 'country']
    search_fields = ['title']


@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ['customer',] 


@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'last_name']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_po']

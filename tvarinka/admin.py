from django.contrib import admin
from .models import ClothingItem, Order

@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'category', 'available', 'created_at')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'clothing_item', 'quantity', 'ordered_at')
    list_filter = ('ordered_at',)
    search_fields = ('customer_name', 'customer_email')

from django.contrib import admin
from .models import Listing

# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    search_fields = ('brands', 'model', 'vin')
    list_filter = ('brands', 'seller')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    
  
from django.contrib import admin
from .models import Buyer, Seller, Product, StoreType, ProductCategory, Transaction

# Register your models here.
class ProductAdmin(admin.StackedInline):
    model = Product
    extra = 3

class SellerAdmin(admin.ModelAdmin):
      fieldsets = [
           (None, {'fields':['store_name', 'location', 'profile_pic',  'user', 'storetype']}),
    
      ]  
      inlines = [ProductAdmin]

admin.site.register(Seller, SellerAdmin)
admin.site.register(Buyer)      
admin.site.register(StoreType)
admin.site.register(ProductCategory)
admin.site.register(Transaction)


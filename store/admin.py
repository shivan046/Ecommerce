from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','digital','image_tag']
    def image_tag(self, obj):
        return format_html('<img src="{}" / width=200>'.format(obj.image.url))

admin.site.register(Customer)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)



from django.contrib import admin
from .models import Shoe, ShoeColor, Manufacturer, ShoeType

admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)
admin.site.register(Manufacturer)
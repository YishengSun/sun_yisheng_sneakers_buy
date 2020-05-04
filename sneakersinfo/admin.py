from django.contrib import admin

from .models import Year, Type, Company, Country, Agency, Sneakers, Order

admin.site.register(Year)
admin.site.register(Type)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Agency)
admin.site.register(Sneakers)
admin.site.register(Order)

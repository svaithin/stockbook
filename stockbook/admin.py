from django.contrib import admin
from stockbook.models import UserProfile, Stocks, Holding
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Stocks)
admin.site.register(Holding)
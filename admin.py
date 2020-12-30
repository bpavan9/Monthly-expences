from django.contrib import admin
from .models import Catgeory,Item,Wallet,Wallet_balance

# Register your models here.
admin.site.register(Catgeory)
admin.site.register(Item)
admin.site.register(Wallet)
admin.site.register(Wallet_balance)

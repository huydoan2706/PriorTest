from django.contrib import admin
from .models import Inventory, Receipt

# Register your models here.
admin.site.register(Receipt)
admin.site.register(Inventory)

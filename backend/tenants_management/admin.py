from django.contrib import admin

from .models import Sector, Tenant


# Register your models here.
admin.site.register(Tenant)
admin.site.register(Sector)
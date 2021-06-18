from django.contrib import admin

# Register your models here.

from .models import Instruments, Calipers, Micrometers

admin.site.register(Instruments)
admin.site.register(Calipers)
admin.site.register(Micrometers)
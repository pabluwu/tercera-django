from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Bombero, Citacion

admin.site.register(Bombero, UserAdmin)
admin.site.register(Citacion)

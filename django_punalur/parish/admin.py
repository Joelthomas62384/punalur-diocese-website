from django.contrib import admin
from . models import parish
# Register your models here.

@admin.register(parish)
class parishAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
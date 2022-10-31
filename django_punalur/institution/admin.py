from django.contrib import admin
from . models import institution
# Register your models here.

@admin.register(institution)
class institutionAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
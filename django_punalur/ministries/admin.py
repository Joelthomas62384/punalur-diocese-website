from django.contrib import admin
from . models import ministry
# Register your models here.

@admin.register(ministry)
class minstryAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
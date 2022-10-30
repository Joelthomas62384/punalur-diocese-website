from django.contrib import admin
from . models import Diocesen_Priest, Relgious_Priest
# Register your models here.
@admin.register(Diocesen_Priest)
class Diocesen_Priest_Admin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)

@admin.register(Relgious_Priest)
class Religious_priest_Admin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
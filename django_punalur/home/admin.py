from django.contrib import admin
from .models import About, Bishop,  Contact, Religious_Women, bibleverse, bishopschedule, bishopvenue, carouselimg, downloads

# Register your models here.
admin.site.register(carouselimg)
admin.site.register(bishopschedule)
admin.site.register(bishopvenue)
admin.site.register(bibleverse)
admin.site.register(Contact)
admin.site.register(Religious_Women)
admin.site.register(downloads)
# admin.site.register(BlogComment)



@admin.register(Bishop)

class BishopAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)


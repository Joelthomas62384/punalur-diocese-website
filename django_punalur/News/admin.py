from django.contrib import admin
from . models import news_Post, newsComment
admin.site.register(newsComment)

@admin.register(news_Post)
class newsAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
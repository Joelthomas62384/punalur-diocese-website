from django.contrib import admin
from . models import Blog_Post, BlogComment


admin.site.register(BlogComment)

@admin.register(Blog_Post)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/tinyInject.js',)
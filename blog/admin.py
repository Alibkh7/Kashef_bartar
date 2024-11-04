from django.contrib import admin
from .models import Article, Category
from django.db import models


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_body', 'created', 'show_image')
    search_fields = ('title',)

    def short_body(self, obj):
        return obj.body[:50] + '...' if len(obj.body) > 50 else obj.body

    short_body.short_description = 'خلاصه متن'




admin.site.register(Category)

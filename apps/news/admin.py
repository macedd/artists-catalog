from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Article information'), {'fields': ['title', 'link', 'image']}),
        (_('Homepage Featured'), {'fields': ['featured']}),
    ]
    list_display = ('title', 'featured', 'created_at')
    list_filter = ['featured', 'created_at']

admin.site.register(Article, ArticleAdmin)

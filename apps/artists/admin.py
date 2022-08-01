from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import Artist, Category, Portfolio

class CategoryInline(admin.TabularInline):                                                                                               
    model = Artist.categories.through

class PortfolioInline(admin.TabularInline):                                                                                               
    model = Portfolio
    extra = 2

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Basic information'), {'fields': ['name', 'title', 'photo']}),
        (_('Categories'), {'fields': ['categories']}),
        (_('Homepage Featured'), {'fields': ['featured']}),
        (_('Extended information'), {'fields': ['biography', 'birth_date', 'birth_city', 'artistic_kinship', 'groups_affiliation', 'works']}),
        (_('Contact information'), {'fields': ['website', 'instagram', 'facebook', 'whatsapp']}),
        (_('Related Artists'), {'fields': ['related']}),
    ]
    inlines = (PortfolioInline,)                                                  
    list_display = ('name', 'title', 'featured', 'created_at')
    list_filter = ['featured', 'created_at']
    filter_horizontal = ('categories', 'related')

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'parent']}),
    ]
    list_display = ('title', 'parent')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio)

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
    list_display = ('name', 'get_categories', 'featured', 'created_at')
    list_filter = ['featured', 'categories', 'created_at']
    filter_horizontal = ('categories', 'related')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('categories')

    def get_categories(self, obj):
        return "\n".join([c.title for c in obj.categories.all()])
    get_categories.short_description = _('Categories')


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'parent']}),
        (_('Homepage Featured'), {'fields': ['featured']}),
    ]
    list_filter = ['featured']
    list_display = ('title', 'parent', 'featured')

class PortfolioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['artist', 'upload_type', 'upload', 'link']}),
    ]
    list_display = ('title', 'upload_type', 'get_artist')
    list_filter = ['upload_type']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('artist')

    def get_artist(self, obj):
        return obj.artist.title
    get_artist.short_description = _('Artist')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Portfolio, PortfolioAdmin)

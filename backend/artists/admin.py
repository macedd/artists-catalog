from django.contrib import admin

# Register your models here.
from .models import Artist, Category

class CategoryInline(admin.TabularInline):                                                                                               
    model = Artist.categories.through


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['name', 'slug', 'title', 'photo']}),
        ('Categories', {'fields': ['categories']}),
        ('Homepage Featured', {'fields': ['featured']}),
        ('Extended information', {'fields': ['biography', 'birth_date', 'birth_city', 'artistic_kinship', 'groups_affiliation', 'works']}),
        ('Contact information', {'fields': ['website', 'instagram', 'facebook', 'whatsapp']}),
    ]
    # inlines = (CategoryInline,)                                                  
    list_display = ('name', 'title', 'featured', 'created_at')
    list_filter = ['featured', 'created_at']

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)

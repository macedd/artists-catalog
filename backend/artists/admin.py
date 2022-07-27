from django.contrib import admin

# Register your models here.
from .models import Artist

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information', {'fields': ['name', 'slug', 'title', 'photo']}),
        ('Homepage Featured', {'fields': ['featured']}),
        ('Extended information', {'fields': ['biography', 'birth_date', 'birth_city', 'artistic_kinship', 'groups_affiliation', 'works']}),
        ('Contact information', {'fields': ['website', 'instagram', 'facebook', 'whatsapp']}),
    ]
    list_display = ('name', 'title', 'featured', 'created_at')
    list_filter = ['featured', 'created_at']

admin.site.register(Artist, ArtistAdmin)

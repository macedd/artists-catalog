from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin

# Create your models here.

def artist_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'artists_{0}/{1}'.format(instance.id, filename)

class Artist(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    title = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=artist_directory_path, blank=True)

    featured = models.BooleanField()
    
    biography = models.TextField()
    birth_date = models.DateField()
    birth_city = models.CharField(max_length=120)

    artistic_kinship = models.TextField(blank=True)
    groups_affiliation = models.TextField(blank=True)
    works = models.TextField(blank=True)

    website = models.CharField(max_length=120, blank=True)
    instagram = models.CharField(max_length=60, blank=True)
    facebook = models.CharField(max_length=60, blank=True)
    whatsapp = models.CharField(max_length=60, blank=True)

    views = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def views_increment(self):
      Artist.objects.filter(id=self.id).update(views=models.F('views') + 1)

    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='Published recently?',
    # )
    def __str__(self):
        return self.name

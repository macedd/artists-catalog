from django.db import models
from django.template.defaultfilters import slugify
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .fields import PortfolioUploadField

# Create your models here.

def artist_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'artists_{0}/{1}'.format(instance.id, filename)

class Artist(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    title = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=artist_directory_path, blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    related = models.ManyToManyField('self', blank=True)

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Category(models.Model):
    title  = models.CharField(max_length=60)
    slug   = models.SlugField(max_length=60)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"
        unique_together = ('slug', 'parent',)    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)

    class UploadTypes(models.TextChoices):
        MUSIC   = 'music', _('Music')
        DRAWING = 'drawing', _('Drawing')
        PHOTO   = 'photo', _('Photo')
        VIDEO   = 'video', _('Video')

    upload_type = models.CharField(
        max_length=10,
        choices=UploadTypes.choices
    )
    upload = PortfolioUploadField(
        upload_to=artist_directory_path,
        blank=True,
        null=True
    )
    link  = models.URLField(
        blank=True,
        null=True
    )

    views = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.upload and not self.link:
            raise ValidationError('Upload or link are required for portfolio')

    def __str__(self):
        return self.title

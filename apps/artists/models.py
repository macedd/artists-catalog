from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .fields import PortfolioUploadField
from apps.library.models import SlugsBase, TimestampsBase, ViewsBase, ThumbnailsBase, VideosBase

# Create your models here.

def artist_directory_path(instance: models.Model, filename: str):
    # intance can be artist or portfolio
    slug = instance.artist.slug_original if hasattr(instance, 'artist') else instance.slug_original
    # file will be uploaded to MEDIA_ROOT/<slug>/<filename>
    return 'artists/{0}/{1}'.format(slug, filename)

class Artist(SlugsBase, TimestampsBase, ViewsBase, ThumbnailsBase):
    name = models.CharField(
        max_length=120,
        verbose_name=_('Name')
    )
    title = models.CharField(
        max_length=60,
        verbose_name=_('Title')
    )
    photo = models.ImageField(
        upload_to=artist_directory_path,
        blank=True,
        verbose_name=_('Photo')
    )

    categories = models.ManyToManyField(
        'Category',
        blank=True,
        verbose_name=_('Categories')
    )
    related = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name=_('Related')
    )

    featured = models.BooleanField(
        verbose_name=_('Featured')
    )
    
    biography = models.TextField(
        verbose_name=_('Biography')
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Birth date')
    )
    birth_city = models.CharField(
        max_length=120,
        verbose_name=_('Birth city')
    )

    artistic_kinship = models.TextField(
        blank=True,
        verbose_name=_('Artistic Kinship')
    )
    groups_affiliation = models.TextField(
        blank=True,
        verbose_name=_('Groups Affiliation')
    )
    works = models.TextField(
        blank=True,
        verbose_name=_('Works')
    )

    website = models.CharField(
        max_length=120,
        blank=True,
        verbose_name=_('Website')
    )
    instagram = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_('Instagram')
    )
    facebook = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_('Facebook')
    )
    whatsapp = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_('Whatsapp')
    )
    youtube = models.CharField(
        max_length=60,
        blank=True,
        verbose_name=_('Youtube')
    )

    def save(self, *args, **kwargs):
        self.make_slug('name')
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')
        
    def __str__(self):
        return self.name
    
    def get(artist_slug):
        try:
            return Artist.objects.get(slug=artist_slug)
        except Artist.DoesNotExist:
            return Artist.objects.get(past_slugs__contains=artist_slug)


class Category(SlugsBase, TimestampsBase):
    title  = models.CharField(
        max_length=60,
        verbose_name=_('Title')
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('Parent category')
    )
    featured = models.BooleanField(
        default=False,
        verbose_name=_('Featured')
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        unique_together = ('slug', 'parent',)    

    def save(self, *args, **kwargs):
        self.make_slug('title')
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Portfolio(TimestampsBase, ThumbnailsBase, VideosBase):
    artist = models.ForeignKey(
        Artist,
        related_name='portfolio', 
        on_delete=models.CASCADE,
        verbose_name=_('Artist')
    )
    title = models.CharField(
        max_length=120,
        blank=True,
        verbose_name=_('Title')
    )

    class UploadTypes(models.TextChoices):
        MUSIC    = 'music', _('Music')
        DRAWING  = 'drawing', _('Drawing')
        PHOTO    = 'photo', _('Photo')
        VIDEO    = 'video', _('Video')
        PAINTING = 'painting', _('Painting')

    upload_type = models.CharField(
        max_length=10,
        choices=UploadTypes.choices,
        verbose_name=_('Upload type')
    )
    upload = PortfolioUploadField(
        upload_to=artist_directory_path,
        blank=True,
        null=True,
        verbose_name=_('Upload')
    )
    link  = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('Link')
    )

    views = models.IntegerField(
        default=0,
        editable=False,
        verbose_name=_('Views')
    )

    def clean(self):
        if not self.upload and not self.link:
            raise ValidationError('Upload or link are required for portfolio')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # caches images
        if self.upload_type in ['drawing', 'photo']:
            self.cache_thumbnails(['upload', 'link'], ['400x400', '1800'])
        # caches videos
        if self.upload_type in ['video']:
            thumbnail = self.get_video_thumbnail('link')
            self.cache_images([thumbnail], ['400x400'])

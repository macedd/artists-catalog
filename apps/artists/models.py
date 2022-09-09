from django.db import models
from django.template.defaultfilters import slugify
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .fields import PortfolioUploadField

# Create your models here.

def artist_directory_path(portfolio, filename):
    # file will be uploaded to MEDIA_ROOT/<slug>/<filename>
    return 'artists/{0}/{1}'.format(portfolio.artist.slug, filename)

class Artist(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name=_('Name')
    )
    slug = models.SlugField(
        max_length=120,
        unique=True,
        verbose_name=_('Slug')
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

    views = models.IntegerField(
        default=0,
        editable=False,
        verbose_name=_('Views')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    def views_increment(self):
      Artist.objects.filter(id=self.id).update(views=models.F('views') + 1)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')
        
    def __str__(self):
        return self.name

class Category(models.Model):
    title  = models.CharField(
        max_length=60,
        verbose_name=_('Title')
    )
    slug   = models.SlugField(
        max_length=60,
        verbose_name=_('Slug')
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('Parent category')
    )

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        unique_together = ('slug', 'parent',)    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        verbose_name=_('Artist')
    )
    title = models.CharField(
        max_length=120,
        verbose_name=_('Title')
    )

    class UploadTypes(models.TextChoices):
        MUSIC   = 'music', _('Music')
        DRAWING = 'drawing', _('Drawing')
        PHOTO   = 'photo', _('Photo')
        VIDEO   = 'video', _('Video')

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
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at')
    )

    def clean(self):
        if not self.upload and not self.link:
            raise ValidationError('Upload or link are required for portfolio')

    def __str__(self):
        return self.title

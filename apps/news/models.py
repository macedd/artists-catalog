from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.library.models import SlugsBase, TimestampsBase, ViewsBase, ThumbnailsBase

def news_directory_path(instance: models.Model, filename: str):
    slug = instance.slug_original
    # file will be uploaded to MEDIA_ROOT/news/<slug>_<filename>
    return 'news/{0}_{1}'.format(slug, filename)

class Article(SlugsBase, TimestampsBase, ViewsBase, ThumbnailsBase):
    title = models.CharField(
        max_length=240,
        verbose_name=_('Title')
    )
    
    link = models.URLField(
        max_length=120,
        verbose_name=_('Hyperlink')
    )
    image = models.ImageField(
        upload_to=news_directory_path,
        verbose_name=_('Image')
    )

    featured = models.BooleanField(
        verbose_name=_('Featured'),
        default=True,
    )

    def save(self, *args, **kwargs):
        self.make_slug('title')
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        
    def __str__(self):
        return self.title

'''
Other models:
- Post / Publication
- Comment
- 
'''
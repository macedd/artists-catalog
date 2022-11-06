from django.db import models
from django.template.defaultfilters import slugify
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def news_directory_path(instance: models.Model, filename: str):
    slug = instance.original_slug
    # file will be uploaded to MEDIA_ROOT/news/<slug>_<filename>
    return 'news/{0}_{1}'.format(slug, filename)

class Article(models.Model):
    title = models.CharField(
        max_length=240,
        verbose_name=_('Name')
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name=_('Slug')
    )
    past_slugs = models.JSONField(
        default=list,
        verbose_name=_('Past Slugs')
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
      Article.objects.filter(id=self.id).update(views=models.F('views') + 1)

    @property
    def original_slug(self):
        return self.past_slugs[0]
    
    def _keep_slug(self):
        self.slug = slugify(self.title)
        # new slug
        if self.slug not in self.past_slugs:
            # todo: make past_slug to be unique (check slug existed in any other artist)
            self.past_slugs.append(slugify(self.title))

    def save(self, *args, **kwargs):
        self._keep_slug()
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
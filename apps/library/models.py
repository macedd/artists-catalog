from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

import sorl.thumbnail

class SlugsBase(models.Model):
  _slug_from = None

  slug = models.SlugField(
    max_length=120,
    unique=True,
    verbose_name=_('Slug')
  )
  past_slugs = models.JSONField(
    default=list,
    verbose_name=_('Past Slugs')
  )

  @property
  def slug_original(self):
    return self.past_slugs[0]

  def save_slug(self):
    self.slug = slugify(getattr(self, self._slug_from))
    # new slug
    if self.slug not in self.past_slugs:
        # todo: make past_slug to be unique (check slug existed in any other artist)
        self.past_slugs.append(slugify(self.title))

  class Meta:
    abstract = True


class TimestampsBase(models.Model):
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('Created at')
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_('Updated at')
  )

  class Meta:
    abstract = True

class ViewsBase(models.Model):
  views = models.IntegerField(
    default=0,
    editable=False,
    verbose_name=_('Views')
  )

  def views_increment(self):
    self.__class__.objects.filter(id=self.id).update(views=models.F('views') + 1)
  
  class Meta:
    abstract = True

class ThumbnailsBase(models.Model):
  images_thumbnails = models.JSONField(
      default=dict,
      verbose_name=_('Images thumbnails')
  )

  def get_image_thumbnail(self, field, size, crop='center'):
    '''
    Caches thumbnail sizes in the model to avoid sorl.thumbnail cache lookup for each image
    '''
    image = getattr(self, field)
    if not image:
      return None
    # cache key for thumbnail
    key = '%s-%s-%s-%s' % (field, size, crop, image)
    if not key in self.images_thumbnails:
      # loads new thumbnail and saves reference
      self.images_thumbnails[key] = sorl.thumbnail.get_thumbnail(image, size, crop=crop, quality=90).url
      self.save(update_fields=['images_thumbnails'])
    # reads thumbnail url from model cache
    return self.images_thumbnails[key]

  class Meta:
    abstract = True

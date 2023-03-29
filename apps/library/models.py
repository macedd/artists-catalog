import urllib.parse as urlparse

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

import sorl.thumbnail

class SlugsBase(models.Model):
  slug = models.SlugField(
    max_length=120,
    unique=True,
    verbose_name=_('Slug')
  )
  past_slugs = models.JSONField(
    default=list,
    verbose_name=_('Past Slugs'),
    editable=False
  )

  @property
  def slug_original(self):
    return self.past_slugs[0]

  def make_slug(self, slug_from):
    self.slug = slugify(getattr(self, slug_from))
    # new slug
    if self.slug not in self.past_slugs:
        # todo: make past_slug to be unique (check slug existed in any other artist)
        self.past_slugs.append(slugify(self.title))

  class Meta:
    abstract = True


class TimestampsBase(models.Model):
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('Created at'),
    editable=False
  )
  updated_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_('Updated at'),
    editable=False
  )

  class Meta:
    abstract = True

class ViewsBase(models.Model):
  views = models.IntegerField(
    default=0,
    editable=False,
    verbose_name=_('Views')
  )

  def increment_views(self):
    self.__class__.objects.filter(id=self.id).update(views=models.F('views') + 1)
  
  class Meta:
    abstract = True

class ThumbnailsBase(models.Model):
  images_thumbnails = models.JSONField(
    default=dict,
    verbose_name=_('Images thumbnails'),
    editable=False
  )

  def get_image_thumbnail(self, field, size, crop='center'):
    '''
    Caches thumbnail sizes in the model to avoid sorl.thumbnail cache lookup for each image
    '''
    image = getattr(self, field)
    if not image:
      return None
    return self.cached_image(image, size, crop, field)

  def cached_image(self, image, size, crop='center', field=None):
    # caches thumbnail for fast access
    key = '%s-%s-%s-%s' % (field, size, crop, image)
    if not key in self.images_thumbnails:
      # loads new thumbnail and saves reference
      self.images_thumbnails[key] = sorl.thumbnail.get_thumbnail(image, size, crop=crop, quality=90).url
      self.save(update_fields=['images_thumbnails'])
    # reads existing thumbnail url from model cache
    return self.images_thumbnails[key]

  def cache_thumbnails(self, fields, sizes):
    for f in fields:
      image = getattr(self, f)
      if not image:
        continue
      for s in sizes:
        self.cached_image(image, s, 'center', f)

  def cache_images(self, images, sizes):
    for i in images:
      if not i:
        continue
      for s in sizes:
        self.cached_image(i, s)

  class Meta:
    abstract = True

class VideosBase(models.Model):

  class Meta:
    abstract = True

  def _youtube_id(self, url):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse.urlparse(url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urlparse.parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None

  def _youtube_thumbnail(self, video_id):
    return f'http://i.ytimg.com/vi/{video_id}s/maxresdefault.jpg'

  def get_video_thumbnail(self, field):
    video = getattr(self, field)
    if not video:
      return None

    ytid = self._youtube_id(video)
    if ytid:
      return self._youtube_thumbnail(ytid)

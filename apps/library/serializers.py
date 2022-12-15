import re
from rest_framework import serializers

class SocialMediaField(serializers.URLField):

  def __init__(self, base_url: str, replaces: list = [], **kwargs):
      super().__init__(**kwargs)
      self.base_url = base_url
      self.replaces = replaces

  def to_representation(self, value):
    value = str(value).strip()
    if value == '':
      return ''
    if value.startswith('http'):
      return value
    # apply cleaning replaces
    for replace in self.replaces:
      value = re.sub(replace[0], replace[1], value)
    # ensures trailing slash on base url
    if re.match(r'^https?:\/\/$', self.base_url):
      base_url = self.base_url
    else:
      base_url = '{0}/'.format(self.base_url.rstrip('/'))
    return '{0}{1}'.format(base_url, value.lstrip('/'))

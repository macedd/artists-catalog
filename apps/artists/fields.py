from django.db import models
from django.core import validators


class PortfolioUploadField(models.FileField):
  def validate(self, value, model_instance):
    super().validate(value, model_instance)

    extensions = []
    if model_instance.upload_type == 'music':
      extensions = ['mp3', 'm4a']
    elif model_instance.upload_type == 'drawing':
      extensions = ['jpg', 'png', 'gif']
    elif model_instance.upload_type == 'photo':
      extensions = ['jpg', 'png', 'gif']
    elif model_instance.upload_type == 'video':
      extensions = ['mpg', 'mpeg', 'mp4']

    validators.FileExtensionValidator(extensions).__call__(value)


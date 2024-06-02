from django.db import models

# Create your models here.

# model for theme
class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.ImageField()
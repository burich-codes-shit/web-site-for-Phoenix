from django.db import models

# Create your models here.


class AllModels(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.FileField(upload_to='all_images')
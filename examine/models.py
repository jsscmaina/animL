from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Guide(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

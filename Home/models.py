from django.db import models
from django.utils.timezone import now
from taggit.managers import TaggableManager

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name











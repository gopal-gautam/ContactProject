from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    query = models.TextField()
    created_timestamp = models.DateTimeField(auto_now=True)
    updated_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


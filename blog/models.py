from django.db import models
from django.contrib import admin
from django_quill.fields import QuillField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=256)
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')
    content = QuillField()

    def __str__(self):
        return self.title

admin.site.register(Blog)
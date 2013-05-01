from django.db import models

# Create your models here.


class posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=80)
    body_text = models.TextField()
    timestamp = models.DateTimeField()

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField(max_length=80)
    content = models.TextField()
    tags = models.CharField(max_length=80)
    status = models.CharField(max_length=80)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'

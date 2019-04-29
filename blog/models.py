import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default='Описание')
    keywords = models.CharField(max_length=120, default='Ключевые слова')
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    like = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='0')
    date = models.DateTimeField(default=datetime.datetime.now)
   # user_count = models.IntegerField(default='0')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % (self.id)

    class Meta:
        ordering = ["-id", "-timestamp"]

"""
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.IntegerField(default='0')
"""
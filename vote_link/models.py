from django.db import models
from django.conf import settings
# Create your models here.

class Link(models.Model):

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Link2(models.Model):

    url = models.CharField(max_length=500)
    author = models.CharField(max_length=500)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('Link', related_name='votes', on_delete=models.CASCADE)

class Vote2(models.Model):
    link = models.ForeignKey('Link2', related_name='votes', on_delete=models.CASCADE)


from django.db import models

class WebPage(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    slug = models.CharField(max_length=128,unique=True)
    # Właściwość `tag_set` pojawi się tu automatycznie !

class Tag(models.Model):
    name = models.CharField(max_length=32)
    pages = models.ManyToManyField(WebPage)

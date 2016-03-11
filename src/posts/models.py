from __future__ import unicode_literals

from django.db import models

# Create your models here.
# MVC MODEL VIEW CONTROLLER:

class Post(models.Model):
    title = models.CharField(max_length = 120) 
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    #unicode allows for the title of the post to put displayed on the posts
    #in admin
    def __unicode__(self):
        return self.title

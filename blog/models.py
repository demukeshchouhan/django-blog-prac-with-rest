from __future__ import unicode_literals

from django.db import models

        



class Post(models.Model):
    title = models.CharField(max_length=145)
    description = models.TextField()
    post_image = models.ImageField(upload_to="static/img/", blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    posts = models.ForeignKey(Post, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message
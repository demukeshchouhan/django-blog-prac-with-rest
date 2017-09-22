from django.contrib import admin
from blog.models import Post, Comment


admin.site.register(Comment)
admin.site.register(Post)
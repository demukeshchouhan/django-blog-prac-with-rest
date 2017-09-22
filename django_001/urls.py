
from django.conf.urls import url, include
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import admin
from blog.models import Post, Comment

# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers

# class PostSerializer(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = Post
#         fields = ('title', 'description', 'post_image', 'likes')
        
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

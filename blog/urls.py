from django.conf.urls import url
from blog.views import blog_post_list,blog_post_detail

urlpatterns = [
    url(r"^posts/$", blog_post_list, name="blog_post_list"),
    url(r"^posts/(?P<pk>\d+)$", blog_post_detail, name="blog_post_detail"),
]
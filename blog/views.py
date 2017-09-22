from django.shortcuts import render
from blog.models import Post, Comment
from . import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def blog_post_list(request):
    data = Post.objects.all()
    context = {
         "data": data
    }
    return render(request, "blog/index.html", context)
    
    
    
def blog_post_detail(request, pk):
    form = forms.CommentForm()
    data = Post.objects.get(id=pk)
    
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.message = form.cleaned_data['message']
            comment.posts_id = data.pk
            comment.save()
            return HttpResponseRedirect(reverse("blog:blog_post_detail", args=[data.pk]))
            
    
    context = {
         "data": data,
         "form":form
    }
    return render(request, "blog/detail.html", context)
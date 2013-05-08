from django.http import HttpResponseRedirect
from django.shortcuts import render

from tuxhe_blog.models import Post
from tuxhe_blog.forms import PostForm


def get_posts(number_of_posts=10):
    posts_total = Post.objects.all().order_by('-create_at')[:number_of_posts]
    return posts_total


def index(request):
    posts = get_posts(5)
    return render(request, 'tuxhe_blog/index.html', {'posts': posts})


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'tuxhe_blog/post.html', {'form': form})

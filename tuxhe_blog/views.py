from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json

from tuxhe_blog.models import Post
from tuxhe_blog.forms import PostForm


def get_posts(number_of_posts=10):
    posts_total = Post.objects.all().order_by('-create_at')[:number_of_posts]
    return posts_total


def index(request):
    posts = get_posts(10)
    return render(
        request,
        'tuxhe_blog/index.html',
        {
            'posts': posts,
            'user': request.user
        })


@login_required
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'tuxhe_blog/post.html', {'form': form})


@login_required
def vote(request):
    print 'postId {%s}' % request.POST['post']
    post = get_object_or_404(Post, pk=request.POST.get('post'))
    post.tags = 'voted'
    post.save()
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'
    return HttpResponse(json.dumps(response_data),
                        content_type="application/json")

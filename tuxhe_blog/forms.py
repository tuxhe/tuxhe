from django.forms import ModelForm

from tuxhe_blog.models import Post


class PostForm(ModelForm):
    """docstring for PostForm"""
    class Meta:
        model = Post
        
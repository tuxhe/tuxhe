from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'tuxhe_blog.views.index', name='index'),
    url(r'^post/$', 'tuxhe_blog.views.post', name='post'),
)

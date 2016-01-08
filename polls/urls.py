from django.conf.urls import patterns,url,include

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post, name='detail'),
    url(r'^(?P<post_id>[0-9]+)/addcomment/$', views.addComment, name = 'addcomment'),
    url(r'^auth/',include('userssys.urls'))
]

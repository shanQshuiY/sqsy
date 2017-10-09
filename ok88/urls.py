from django.conf.urls import url
from ok88 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<article_id>[\w\-]+)/$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
]
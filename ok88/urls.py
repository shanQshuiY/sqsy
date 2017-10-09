from django.conf.urls import url
from ok88 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
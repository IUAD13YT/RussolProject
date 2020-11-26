from django.conf.urls import url

from AdVITO import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
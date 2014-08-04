from django.conf.urls import patterns, url
import views

__author__ = 'brentpayne'

urlpatterns = patterns('',
    url(r'^sum/(?P<a>[^/]+)/(?P<b>\d+)/$', views.sum_task)
)

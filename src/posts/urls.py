from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
    )

urlpatterns = [
    url(r'^create/$', post_list), #'posts.views.post_create'),
    url(r'^detail/$', post_detail), #'posts.views.post_detail'),
    url(r'^$', post_list), #'posts.views.post_list'),
    url(r'^delete/$', post_delete), #'posts.views.post_delete'),
    # url(r'^admin/', appname.views.functionname),
]

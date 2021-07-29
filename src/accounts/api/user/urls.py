from django.contrib import admin
from django.urls import path, re_path, include

from .views import UserDetailApiView, UserStatusApiView

urlpatterns = [
    re_path(r'^(?P<username>\w+)/$', UserDetailApiView.as_view(), name = 'detail'),
    re_path(r'^(?P<username>\w+)/status/$', UserStatusApiView.as_view(), name = 'detail-list'),
]

app_name = 'accounts'
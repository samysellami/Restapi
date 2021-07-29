from django.contrib import admin
from django.urls import path, re_path, include
from .views import ( 
    StatusAPIView,
    StatusAPIDetailView 
)

urlpatterns = [
    re_path(r'^$', StatusAPIView.as_view(), name = 'list'),
    re_path(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name = 'detail'),
]

app_name = 'status'

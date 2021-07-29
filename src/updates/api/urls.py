
from django.urls import path, re_path

from .views import (
    UpateModelDetailApiView,
    UpateModelListApiView
)

urlpatterns = [
    re_path(r'^$', UpateModelListApiView.as_view()), # api/updates -> list, create
    re_path(r'^(?P<id>\d+)/$', UpateModelDetailApiView.as_view()),
]

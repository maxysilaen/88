from django.conf.urls import url
from django.contrib import admin

from .views import (
    TaskListAPIView,
    TaskCreateApiView,
    TaskDetailAPIView
    )

urlpatterns = [
    url(r'^task-list/$', TaskListAPIView.as_view(), name='task-list-api'),
    url(r'^task-create/$', TaskCreateApiView.as_view(), name='task-create-api'),
    url(r'^task-detail/(?P<id>\d+)/$',TaskDetailAPIView.as_view(),name='task-detail-api',
),
]

from django.conf.urls import url
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserListAPIView,
    UserDetailAPIView
    )

urlpatterns = [
    url(r'^user-list/$', UserListAPIView.as_view(), name='user-list'),
    url(r'^user-detail/(?P<pk>[\w-]+)/$', UserDetailAPIView.as_view(), name='user-detail'),

    url(r'^register/$', UserCreateAPIView.as_view(), name='register-api'),
    url(r'^login/$', 'rest_framework_jwt.views.obtain_jwt_token', name='auth_login_api'),
]

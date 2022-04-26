#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.DecoratedTokenRefreshView.as_view(), name='token_refresh'),
]

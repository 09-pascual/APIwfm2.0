from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from wfmapi.views import register
from wfmapi.models import User

router = routers.DefaultRouter(trailing_slash=False)
# Register viewsets


urlpatterns = [
    path('', include(router.urls)),
    path('register', register.register_user),
    path('login', register.login_user),
    path('users', User)
]


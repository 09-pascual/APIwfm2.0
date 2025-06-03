from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from wfmapi.views import register
from wfmapi.views import ClientViewSet, GroupViewset, ProjectViewSet, UserViewSet, WorkerViewSet, ProjectWorkerViewSet, GroupWorkerViewSet, ProjectGroupViewSet  
from wfmapi.views.user import get_current_user
from wfmapi.views.projects import get_my_projects

router = routers.DefaultRouter(trailing_slash=False)
# Register viewsets
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'groups', GroupViewset)
router.register(r'project', ProjectViewSet)
router.register(r'project-workers', ProjectWorkerViewSet)
router.register(r'group-workers', GroupWorkerViewSet)
router.register(r'project-groups', ProjectGroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', register.register_user),
    path('login', register.login_user),
    path('users/me/', get_current_user),
    path('my-projects/', get_my_projects)
]


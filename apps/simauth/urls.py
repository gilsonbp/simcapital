from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.simauth import views

app_name = 'simauth'

router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')

urlpatterns = [
    path('', include(router.urls)),
]

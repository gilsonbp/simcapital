from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.capital import views

app_name = 'capital'

router = DefaultRouter()
router.register(r'users', views.CapitalUserViewSet, base_name='users')
router.register(r'salaries', views.SalaryViewSet, base_name='salaries')

urlpatterns = [
    path('', include(router.urls)),
]

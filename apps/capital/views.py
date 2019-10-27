from rest_framework import viewsets

from apps.capital.models import CapitalUser, Salary
from apps.capital.serializers import CapitalUserSerializer, SalarySerializer


class CapitalUserViewSet(viewsets.ModelViewSet):
    serializer_class = CapitalUserSerializer
    queryset = CapitalUser.objects.all()


class SalaryViewSet(viewsets.ModelViewSet):
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()

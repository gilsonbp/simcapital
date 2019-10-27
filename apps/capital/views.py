from rest_framework import viewsets, filters

from apps.capital.models import CapitalUser, Salary
from apps.capital.serializers import CapitalUserSerializer, SalarySerializer


class CapitalUserViewSet(viewsets.ModelViewSet):
    serializer_class = CapitalUserSerializer
    queryset = CapitalUser.objects.all()


class SalaryViewSet(viewsets.ModelViewSet):
    serializer_class = SalarySerializer
    queryset = Salary.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['capital_user__cpf', 'capital_user__email',
                     'capital_user__name']
    ordering_fields = ['salary_date', 'capital_user__name']

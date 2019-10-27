from rest_framework import viewsets

from apps.capital.models import CapitalUser
from apps.capital.serializers import CapitalUserSerializer


class CapitalUserViewSet(viewsets.ModelViewSet):
    serializer_class = CapitalUserSerializer
    queryset = CapitalUser.objects.all()

from rest_framework import viewsets

from apps.simauth.models import User
from apps.simauth.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

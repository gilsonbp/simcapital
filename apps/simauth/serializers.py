from rest_framework import serializers

from apps.simauth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'id', 'email', 'name', 'is_superuser', 'password'
        )

    def create(self, validated_data):
        if validated_data.get('is_superuser', False):
            user = User.objects.create_superuser(
                validated_data['email'],
                validated_data['name'],
                validated_data['password'],
            )
        else:
            user = User.objects.create_user(
                validated_data['email'],
                validated_data['name'],
                validated_data['password'],
            )

        return user

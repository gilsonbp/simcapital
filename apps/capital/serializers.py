from rest_framework import serializers

from apps.capital.models import CapitalUser


class CapitalUserSerializer(serializers.ModelSerializer):
    avg_salary = serializers.SerializerMethodField(read_only=True)
    avg_discount = serializers.SerializerMethodField(read_only=True)
    max_salary = serializers.SerializerMethodField(read_only=True)
    min_salary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CapitalUser
        fields = (
            'id', 'email', 'name', 'cpf', 'birth_date', 'avg_salary',
            'avg_discount', 'max_salary', 'min_salary'
        )

    def get_avg_salary(self, obj):
        return obj.get_avg_salary()

    def get_avg_discount(self, obj):
        return obj.get_avg_discount()

    def get_max_salary(self, obj):
        return obj.get_max_salary()

    def get_min_salary(self, obj):
        return obj.get_min_salary()

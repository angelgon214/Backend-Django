from rest_framework import serializers
from carros.models import Carros

class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = '__all__'


def validate_plate(self, value):
        if len(value) != 7:
            raise serializers.ValidationError("La placa debe tener 7 caracteres.")
        return value



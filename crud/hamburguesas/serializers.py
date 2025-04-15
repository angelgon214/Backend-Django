from rest_framework import serializers
from hamburguesas.models import Hamburguesa

class HamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = '__all__'
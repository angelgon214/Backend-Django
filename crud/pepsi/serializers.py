from rest_framework import serializers
from pepsi.models import Pepsi

class PepsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pepsi
        fields = '__all__'
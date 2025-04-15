from .models import Carros
from rest_framework import viewsets, permissions
from .serializers import CarrosSerializer  

class CarrosViewSet(viewsets.ModelViewSet):
    queryset = Carros.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarrosSerializer

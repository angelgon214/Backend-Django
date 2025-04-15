from .models import Hamburguesa
from rest_framework import viewsets, permissions
from .serializers import HamburguesaSerializer 

class HamburguesaViewSet(viewsets.ModelViewSet):    
    queryset = Hamburguesa.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HamburguesaSerializer


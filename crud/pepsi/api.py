from .models import Pepsi
from rest_framework import viewsets, permissions
from .serializers import PepsiSerializer

class PepsiViewSet(viewsets.ModelViewSet):
    queryset = Pepsi.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PepsiSerializer

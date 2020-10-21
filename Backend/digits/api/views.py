from rest_framework import viewsets
from .serializers import DigitSerializer
from ..models import Digit

class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitSerializer
    queryset = Digit.objects.all()
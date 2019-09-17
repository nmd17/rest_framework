from rest_framework import viewsets
from .serializers import ShoeColorSerializer, ShoeTypeSerializer, ShoeSerializer, ManufacturerSerializer
from .models import Shoe, ShoeColor, ShoeType, Manufacturer

class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer








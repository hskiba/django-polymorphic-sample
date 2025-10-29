from rest_framework import viewsets
from .models import Base, Currency
from .serializers import BasePolymorphicSerializer, CurrencySerializer


class BaseViewSet(viewsets.ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = BasePolymorphicSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
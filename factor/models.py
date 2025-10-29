from django.db import models
from polymorphic.models import PolymorphicModel

class Base(PolymorphicModel):
    name = models.CharField(max_length=32)

class FX(Base):
    to_currency = models.CharField(max_length=3)
    from_currency = models.CharField(max_length=3)

class Volatility(Base):
    base_factor = models.ForeignKey(Base, on_delete=models.CASCADE)

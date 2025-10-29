from django.db import models
from polymorphic.models import PolymorphicModel

class Base(PolymorphicModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.code

class FX(Base):
    to_currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, related_name="fx_to_currency")
    from_currency = models.ForeignKey(Currency, on_delete=models.RESTRICT, related_name="fx_from_currency")

class Volatility(Base):
    base_factor = models.OneToOneField(Base, on_delete=models.RESTRICT, related_name="volatility_factor")

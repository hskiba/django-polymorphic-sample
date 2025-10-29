from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import Base, FX, Volatility, Currency


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class FXSerializer(serializers.ModelSerializer):
    class Meta:
        model = FX
        fields = "__all__"


class VolatilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Volatility
        fields = "__all__"


class BasePolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'factor_type'
    model_serializer_mapping = {
        Base: BaseSerializer,
        FX: FXSerializer,
        Volatility: VolatilitySerializer
    }
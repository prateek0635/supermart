from rest_framework import serializers
from .models import items,cart


class itemsSerializers(serializers.ModelSerializer):
    class Meta:
        model=items
        fields='__all__'


class cartSerializers(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields='__all__'
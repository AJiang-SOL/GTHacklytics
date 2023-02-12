from rest_framework import serializers
from .model import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("food")

class CreateFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        field = ('file')
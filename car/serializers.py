from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1914)],
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(allow_null=True, allow_blank=True)

    def create(self, validated_data: dict) -> Car:
        return Car.objects.create(**validated_data)

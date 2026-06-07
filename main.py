import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializers = CarSerializer(car)
    return JSONRenderer().render(serializers.data)


def deserialize_car_object(json: bytes) -> Car:
    json = io.BytesIO(json)
    parser = JSONParser().parse(json)
    serializer = CarSerializer(data=parser)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    return instance

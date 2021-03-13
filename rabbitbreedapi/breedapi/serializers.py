from rest_framework import serializers
from .models import Breed


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ('breed_id', 'name', 'image', 'sizes', 'fur_type',
                  'ear_type', 'colors', 'ARBA_recognised', 'BRC_recognised', 'origins')

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BreedSerializer
from .models import Breed


class BreedViewSet(viewsets.ModelViewSet):

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    """Only GET method allowed from unauthorised users"""
    http_method_names = ['get']

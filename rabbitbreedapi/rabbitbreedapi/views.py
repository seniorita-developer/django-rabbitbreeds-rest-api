from rest_framework import viewsets
from .serializers import BreedSerializer
from .models import Breed
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import generics


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    """Only GET method allowed from unauthorised users"""
    http_method_names = ['get']


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class BreedsWithImagesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Breed.objects.filter(image__contains='.jpg')
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class GetRandomBreed(generics.ListAPIView):
    queryset = Breed.objects.all().order_by('?')[:1]
    serializer_class = BreedSerializer

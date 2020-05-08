from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from breedapi import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rabbitbreedapi import settings

router = routers.DefaultRouter()
router.register(r'breeds', views.BreedViewSet)
router.register(r'breeds-with-images', views.BreedsWithImagesViewSet, basename='breeds-with-images')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('random/', views.GetRandomBreed.as_view(), name="random"),
    path('docs/', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

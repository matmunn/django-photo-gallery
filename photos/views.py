import json

from django.http import JsonResponse
from django.shortcuts import render

from .models import Photo


def index(request):
    return render(request, 'photos/index.html', {})


def get_photos(request):
    objects = Photo.objects.all()
    return JsonResponse({'photos': [photo.image.url for photo in objects]})

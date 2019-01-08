from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.get_photos, name='get_photos'),
]

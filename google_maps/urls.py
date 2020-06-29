from django.urls import path

from google_maps import views

urlpatterns = [
    path('', views.default_map, name="default"),
]
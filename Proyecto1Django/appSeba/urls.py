from django.urls import path
from . import views


urlpatterns = [
    path('inicio1/', views.index),
    path('inicio2/',views.index2)
]
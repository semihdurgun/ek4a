from django.http.response import JsonResponse
from django.urls import path
from .views import index

app_name = 'ek4a'

urlpatterns = [
    path('', index, name='index'),
]
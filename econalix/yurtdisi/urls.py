from django.http.response import JsonResponse
from django.urls import path
from .views import index
from django.conf.urls.static import static
from django.conf import settings
app_name = 'yurtdisi'

urlpatterns = [
    path('', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
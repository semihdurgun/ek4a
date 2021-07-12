from django.urls import path
from .views import index, json_duzenlenen, json_eklenen, json_bantcikan, json_cikarilan, json_aktiflenen, json_pasiflenen, json_bant_dahil_edilen   

app_name = 'ek4a'

urlpatterns = [
    path('', index, name='index'),
    path('rapor/eklenen/', json_eklenen, name='index'),
    path('rapor/duzenlenen/', json_duzenlenen, name='index'),
    path('rapor/bantcikan/', json_bantcikan, name='index'),
    path('rapor/cikarilan/', json_cikarilan, name='index'),
    path('rapor/aktiflenen/', json_aktiflenen, name='index'),
    path('rapor/pasiflenen/', json_pasiflenen, name='index'),
    path('rapor/bant_dahil_edilen/', json_bant_dahil_edilen, name='index'),
    #path('rapor/<int:tarih>/cikarilan/', json_cikarilan, name='json_cikarilan'), views jsoncikarilan parametre lazım
]
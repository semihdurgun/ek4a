from django.urls import path
from .views import index, json_duzenlenen, json_eklenen, json_bantcikan, json_cikarilan, json_aktiflenen, json_pasiflenen, json_bant_dahil_edilen   , redirect_to_year
app_name = 'ek4a'

urlpatterns = [
    path('', redirect_to_year, name='index'),
    path('<int:year>/<int:week>', index, name='year-index'),
    path('rapor/eklenen/<int:year>/<int:week>', json_eklenen, name='index'),
    path('rapor/duzenlenen/<int:year>/<int:week>', json_duzenlenen, name='index'),
    path('rapor/bantcikan/<int:year>/<int:week>', json_bantcikan, name='index'),
    path('rapor/cikarilan/<int:year>/<int:week>', json_cikarilan, name='index'),
    path('rapor/aktiflenen/<int:year>/<int:week>', json_aktiflenen, name='index'),
    path('rapor/pasiflenen/<int:year>/<int:week>', json_pasiflenen, name='index'),
    path('rapor/bant_dahil_edilen/<int:year>/<int:week>', json_bant_dahil_edilen, name='index'),
    #path('rapor/<int:tarih>/cikarilan/', json_cikarilan, name='json_cikarilan'), views jsoncikarilan parametre lazım
]
from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path
from .excel_read import excel_read_and_save
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

def redirect_to_year(request):
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    return HttpResponseRedirect(reverse('ek4a:year-index', args=(year,week_num,)))

def index(request,year,week):
    if (excel_read_and_save('',year,week) == -1):
        return render(request, '404.html',)
    return render(request, 'index.html',)

def json_duzenlenen(request,year,week):
    data = {
        "data":excel_read_and_save('4A DÜZENLENENLER',year,week)
    }
    return JsonResponse(data)

def json_eklenen(request,year,week):
    data = {
        "data":excel_read_and_save('4A EKLENENLER',year,week)
    }
    return JsonResponse(data)

def json_bantcikan(request,year,week):
    data = {
       "data":excel_read_and_save('BANT HESABINDAN ÇIKANLAR',year,week)
    }
    return JsonResponse(data)

def json_cikarilan(request,year,week):
    data = {
        "data":excel_read_and_save('4A ÇIKARILANLAR',year,week)
    }
    return JsonResponse(data)

def json_aktiflenen(request,year,week):
    data = {
        "data":excel_read_and_save('4A AKTİFLENENLER',year,week)
    }
    return JsonResponse(data)

def json_pasiflenen(request,year,week):
    data = {
        "data":excel_read_and_save('4A PASİFLENENLER',year,week)
    }
    return JsonResponse(data)

def json_bant_dahil_edilen(request,year,week):
    data = {
        "data":excel_read_and_save('4A BANT HESABA DAHİL EDİLENLER',year,week)
    }
    return JsonResponse(data)


       
 #subtables için -> data = {
 #       "data":[{'Kamu No': 'A18253', 'guncel_barkod': 8682109004039, 'Ürün Adı': 'OXYNAZ %0,01 PEDIATRIK BURUN SPREYI, COZELTI', 'Eski Barkod-1': 'None', 'Eski Barkod-2': 'None', 'Eşdeğer (Benzer) Ürün Grubu': 'E270D', 'Referans Fiyat Grubu': 'None', 'Listeye Giriş Tarihi': 1621209600000, 'Aktiflenme Tarihi': 'None', 'Pasiflenme Tarihi': 'None', 'Orijinal / Jenerik / Yirmi Yıllık': 'YİRMİ YIL', 'Depocuya Satış  Fiyatı\n23,81 TL ve üzeri ise': 0.28, 'Depocuya Satış  Fiyatı \n15,81 TL (dahil) ile 23,80 TL (dahil) arasında ise': 0.1, 
#'Depocuya Satış  Fiyatı \n8,26 TL (dahil) ile 15,80 TL (dahil) arasında ise': 0.0, 'Depocuya Satış Fiyatı \n8,25 TL ve altında ise': 0, 'Özel İskonto': 'None', 'Eczacı İndirim Oranı ': '0-2,5%', ' Band Hesabı Takibinin Başlangıç Tarihi': '17/05/2021', 'Firma Tarafından Dağıtım Belgesinin Bildirileceği Son Tarih': 'None',"changes":{"Kamu Fiyatı":["60.75 TRY","42.53 TRY",-30.0],"Depocu Fiyatı":["67.50 TRY","47.25 TRY",-30.0],"Eczacı Fiyatı":["84.38 TRY","59.06 TRY",-30.0],"Perakende Fiyatı":["91.13 TRY","63.79 TRY",-30.0],"Depocu Kamu Fiyatı":["48.60 TRY","34.02 TRY",-30.0],"İmalatçı Fiyatı":["62.53 TRY","43.66 TRY",-30.2],"İmalatçı Kamu Fiyatı":["45.02 TRY","31.44 TRY",-30.2]}}]
#    }
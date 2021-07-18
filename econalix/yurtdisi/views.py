from django.shortcuts import render
from pathlib import Path
from .excel_read import excel_read_and_save
from django.http import JsonResponse
import json
# Create your views here.

def index(request, *args, **kwargs):
    my_barcode = ''
    data = {
            'item1': 1,
            'item2': 2,
}
    data['item4'] ={"ALDURAYZME":["100 TRY","42 TRY",30.0]}
    if request.method == 'POST':
        my_barcode = request.POST['my_barcode']
        data = excel_read_and_save(my_barcode)

    return render(request, 'yurtdisi.html',{'data':data}) 
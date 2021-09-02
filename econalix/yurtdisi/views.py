from econalix.settings import BASE_DIR
from django.shortcuts import render
import json

# Create your views here.

def index(request, *args, **kwargs):

    with open(BASE_DIR / 'greece-italy-spain.json', 'r') as f:
      data = json.loads(f.read())

    return render(request, 'yurtdisi.html',{'data':data}) 

def index2(request, *args, **kwargs):

    with open(BASE_DIR / 'greece-italy-spain_optimizationed.json', 'r') as f:
      data = json.loads(f.read())

    return render(request, 'yurtdisi.html',{'data':data}) 
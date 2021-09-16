from econalix.settings import BASE_DIR
from django.shortcuts import render
import json

# Create your views here.

def index(request, *args, **kwargs):

    with open(BASE_DIR / 'ALL.json', 'r') as f:
      data = json.loads(f.read())

    return render(request, 'yurtdisi.html',{'data':data}) 

def optimizationed(request, *args, **kwargs):

    with open(BASE_DIR / 'ALL_optimizationed.json', 'r') as f:
      data = json.loads(f.read())

    return render(request, 'yurtdisi.html',{'data':data}) 
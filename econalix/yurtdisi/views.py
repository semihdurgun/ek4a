from econalix.settings import BASE_DIR
from django.shortcuts import render
import json
from pathlib import Path

# Create your views here.

def index(request, *args, **kwargs):

    with open(BASE_DIR / 'yunanistan_json.json', 'r') as f:
      data = json.loads(f.read())

    return render(request, 'yurtdisi.html',{'data':data}) 
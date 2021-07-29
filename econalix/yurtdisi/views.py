from django.shortcuts import render
import json
# Create your views here.

def index(request, *args, **kwargs):

    with open('.\\yunanistan_json.json', 'r') as f:
      data = json.loads(f.read())

    return render(request, 'yurtdisi.html',{'data':data}) 
from django.views.generic import TemplateView
from django.shortcuts import render
import requests

from templates.includes import index_base 

def post(self, request):
 
    headers = {
        'X-Cisco-Meraki-API-Key': '920a310b87feb3832739a79d573845404c6825d0',
        'Content-Type': 'application/json',
    }

    response = requests.post('https://api.meraki.com/api/v1/devices/Q2HV-B24V-ZKN5/camera/generateSnapshot', headers=headers)

    return render(request, 'index_base.html',{'out':response})


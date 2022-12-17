from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import json
import secrets

from . import models

def upload(request):
    body_dict = json.loads(request.body.decode('utf-8'))
    code = body_dict.get('code', '')
    return HttpResponse(status=200)
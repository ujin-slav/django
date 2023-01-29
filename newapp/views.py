from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt 
def index(request):
    print(json.loads(request.body))
    return JsonResponse({"name": "Tom", "age": 38})
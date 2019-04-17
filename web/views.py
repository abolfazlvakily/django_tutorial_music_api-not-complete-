from django.shortcuts import render, get_object_or_404
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Track
from django.core import serializers
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def submit_expense(request):
    print(request.POST)
    return JsonResponse({'ss':'ssss'}, encoder=JSONEncoder, safe=False)

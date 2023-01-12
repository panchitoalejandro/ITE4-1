from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime



def store(request):
    return render(request, 'store/store.html')
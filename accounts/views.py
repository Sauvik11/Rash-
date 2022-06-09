
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from tablib import Dataset
from .models import carModel
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


def dashboard(request):
  cardata= carModel.objects.all()
  bootspace=[]
  price=[]
  for q in cardata:
    print ("q.make",q.make)
    bspce=q.bootSpacelt
    cost=q.price
    bootspace.append(bspce)
    price.append(cost)

  print("price", len(price))
  print("price", len(bootspace))  
  return render(request, 'home.html', {'cardata': cardata,'bootspace': bootspace ,'price': price })



# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

def informacoes(request):
	return render(request, 'informacoes.html')
# Create your views here.



# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Distrito
from .models import Municipio

def index(request):
	return render(request, 'index.html')

def informacoes(request):
	
	return render(request, 'informacoes.html')

def lista_destinos(request):
	distritos = Distrito.objects.all()
	municipios = Municipio.objects.all()

	if request.method == 'GET':
		if 'destinoget' in request.GET:
			destinoget=request.GET.get("destinoget")
		else:
			destinoget=""

		if 'destinoget' in request.GET and request.GET.get("destinoget")!="":
			destinoget=request.GET.get("destinoget")
		else:
			destinoget=Distrito.objects.values_list('id')

	else:
		destinos = Distrito.objects.all()


	context = {
		'distritos': distritos,
		'municipios' : municipios,
		'destinos' : destinos,
		#'nome': nome
	}
	return render(request, 'lista_destinos.html', context)


# Create your views here.



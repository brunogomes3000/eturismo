# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Distrito

def index(request):
	return render(request, 'index.html')

def informacoes(request):
	
	return render(request, 'informacoes.html')

def lista_destinos(request):
	nome = request.GET.get("destino")
	distritos = Distrito.objects.filter(descricao__icontains=nome)

	context = {
		'distritos': distritos
		#'nome': nome
	}
	return render(request, 'lista_destinos.html', context)


<<<<<<< HEAD
=======
	
	return render(request, 'lista_destinos.html')
>>>>>>> 2ac597638b19e2c1b6e59b7da135c89df971f7d3
# Create your views here.



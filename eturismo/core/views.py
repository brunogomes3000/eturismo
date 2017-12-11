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
# Create your views here.
>>>>>>> 4e62d47f2b35013b298f2d781d3856e519dd5d81



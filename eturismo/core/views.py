# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

def informacoes(request):
	#receber via get o nome do destino digitado
	# pesquisar com GET o destino
	# enviar para a página informações o objetco recuperado via context


	return render(request, 'informacoes.html')

# Create your views here.



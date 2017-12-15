# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Distrito
from .models import Municipio
from .models import Dica
from .models import Passeio
from .models import Promocao
from .models import Avaliacao
from .models import Tipo_Passeio
from .models import Empresa


def index(request):
	return render(request, 'index.html')

def informacoes(request):
	id_distrito = request.GET.get("id")
	
	distrito = Distrito.objects.get(id=id_distrito)
	'''municipios = Municipio.objects.filter(Municipio__id__in=distrito.Municipio.id)'''

	dicas = Dica.objects.filter(Distrito__id__in=id_distrito)
	passeios = Passeio.objects.filter(Distrito__id__in=id_distrito)
	promocoes = Promocao.objects.filter(Distrito__id__in=id_distrito)
	avaliacoes = Avaliacao.objects.filter(Distrito__id__in=id_distrito)
	
	context = {
		'distrito': distrito,
		'dicas': dicas,
		'passeios': passeios,
		'promocoes': promocoes,
		'avaliacoes': avaliacoes
	}
	return render(request, 'informacoes.html', context)

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
		
		#'nome': nome
	}
	return render(request, 'lista_destinos.html', context)

def passeio_detalhes(request):
	passeio = Passeio.objects.all()
	empresa = Empresa.objects.all()
	
	if request.method == 'GET':
	if 'nomeget' in request.GET: nomeget=request.GET.get("nomeget")
		else:
		nomeget=""

	if 'passeioget' in request.GET and request.GET.get("passeioget")!="":passeioget=request.GET.get("passeioget")
	
		else:
		publicoget=Publico.objects.values_list('id')
	
	if 'empresaget' in request.GET and request.GET.get("empresaget")!="": empresaget=request.GET.get("empresaget")
		empresaget=request.GET.get("empresaget")
		else:
			empresaget=Empresa.objects.values_list('id')
			passeio = Passeio.objects.filter(nome__icontains=nomeget, area__id__in=empresaget, passeio__id__in=passeioget).distinct()
		else:
		passeio = Passeio.objects.all()

	context = {
		'passeio': passeio,
		'empresa': empresa,
	}

	return render(request, 'passeio_detalhes.html', context)

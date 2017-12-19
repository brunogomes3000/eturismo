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
from django.contrib.auth.forms import UserCreationForm


def index(request):
	return render(request, 'index.html')

def informacoes(request):
	id_distrito = request.GET.get("id")
	distrito = Distrito.objects.get(id=id_distrito)
	tipo_passeio = Tipo_Passeio.objects.all()

	form = UserCreationForm(request.POST or None)
	
	
	passeios = Passeio.objects.filter(Distrito__id__in=id_distrito)
	#municipios = Municipio.objects.get(Distrito__id__in=id_distrito)

	#passeio = Passeio.objects.filter(Distrito__id__in=id_distrito)
	dicas = Dica.objects.filter(Distrito__id__in=id_distrito)
	promocoes = Promocao.objects.filter(Distrito__id__in=id_distrito)
	avaliacoes = Avaliacao.objects.filter(Distrito__id__in=id_distrito)

	if request.method == 'GET':
		if 'descricaoget' in request.GET:
				descricaoget=request.GET.get("descricaoget")
		else:
			descricaoget=""

		if 'passeioget' in request.GET and request.GET.get("passeioget")!="": 
			passeioget=request.GET.get("passeioget")
		else:
			passeioget=Tipo_Passeio.objects.values_list('id')
			passeio = Tipo_Passeio.objects.filter(descricao__icontains=descricaoget, passeio__id__in=passeioget).distinct()
	
	else:
		passeio = Tipo_Passeio.objects.all()
		
	context = {

		'distrito': distrito,
		'dicas': dicas,
		'passeios': passeios,
		'promocoes': promocoes,
		'avaliacoes': avaliacoes,
		'tipo_passeio' : tipo_passeio,
		'form': form,	
	}

		
	if request.method == 'POST':
		if form.is_valid():
			form.save()
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
	id_passeio = request.GET.get("id")
	passeio = Passeio.objects.get(id=id_passeio)

	context = {
		'passeio': passeio
	
		}

	return render(request, 'passeio_detalhes.html', context)


	
	

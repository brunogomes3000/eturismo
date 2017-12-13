# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Distrito
from .models import Municipio

def index(request):
	return render(request, 'index.html')

def informacoes(request):
	id_informacoes = request.GET.get("id")
	
	id_municipioinfo = request.GET.get("id")
	municipioinfo = Municipio.objects.get(id=id_municipioinfo)

	id_dicainfo = request.GET.get("id")
	dicainfo = Dica.objects.get(id=id_dicainfo)

	id_passeioinfo = request.GET.get("id")
	passeioinfo = Passeio.objects.get(id=id_passeioinfo)

	id_promocaoinfo = request.GET.get("id")
	promocaoinfo = Promocao.objects.get(id=id_promocaoinfo)

	id_avaliacaoinfo = request.GET.get("id")
	avaliacaoinfo = Avaliacao.objects.get(id=id_avaliacaoinfo)

	id_enderecoinfor = request.GET.get("id")
	enderecoinfor = Endereco.objects.get(id=id_enderecoinfo)

	id_contatoinfor = request.GET.get("id")
	contatoinfor = Contato.objects.get(id=id_contatoinfo)

	id_tipodicainfor = request.GET.get("id")
	tipodicainfor = Tipo_Dica.objects.get(id=id_tipodicainfo)

	context = {
	'municipioinfo': municipioinfo,
	'dicainfo': dicainfo,
	'passeioinfo': passeioinfo,
	'promocaoinfo': promocaoinfo,
	'avaliacaoinfo': avaliacaoinfo,
	'enderecoinfor': enderecoinfor,
	'contatoinfor': contatoinfor,
	'tipodicainfor': tipodicainfor,
}
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
		
		#'nome': nome
	}
	return render(request, 'lista_destinos.html', context)

def passeio_detalhes(request):

	return render(request, 'passeio_detalhes.html')
# Create your views here.



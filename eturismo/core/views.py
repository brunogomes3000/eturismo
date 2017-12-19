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
from .forms import AvaliacaoModelForm



def index(request):
	return render(request, 'index.html')

def informacoes(request):
	
	if request.method == 'GET':
		id_distrito = request.GET.get("id")
		distrito = Distrito.objects.get(id=id_distrito)
		if 'id' in request.GET:
			id_distrito = request.GET.get("id")
			distrito = Distrito.objects.get(id=id_distrito)
		
		passeios = Passeio.objects.filter(Distrito__id__in=id_distrito)
		#municipios = Municipio.objects.get(Distrito__id__in=id_distrito)

		#passeio = Passeio.objects.filter(Distrito__id__in=id_distrito)
		dicas = Dica.objects.filter(Distrito__id__in=id_distrito)
		promocoes = Promocao.objects.filter(Distrito__id__in=id_distrito)
		avaliacoes = Avaliacao.objects.filter(Distrito__id__in=id_distrito)
		tipo_passeio=Tipo_Passeio.objects.all()

		if request.method == 'GET':
			if 'descricaoget' in request.GET:
					descricaoget=request.GET.get("descricaoget")
			else:
				descricaoget=""

			if 'passeioget' in request.GET and request.GET.get("passeioget")!="": 
				passeioget=request.GET.get("passeioget")
			else:
				passeioget=Tipo_Passeio.objects.values_list('id')
			
			passeios = Passeio.objects.filter(descricao__icontains=descricaoget, Tipo_Passeio__id__in=passeioget).distinct()
		
		

		#Enviando o formulario para a página

	
	#Aqui vai ficar o código de armazenamento da avaliacao (seguir tutorial a partir do VINCULAR UM CADASTRO DE USUÁRIO(ADMIN) À CLASSES DO BANCO)


		
	context = {
		'distrito': distrito,
		'dicas': dicas,
		'passeios': passeios,
		'promocoes': promocoes,
		'avaliacoes': avaliacoes,
		'tipo_passeio' : tipo_passeio,
		
	}

	return render(request, 'informacoes.html', context)

def lista_destinos(request):
	#distritos = Distrito.objects.all()

	#distritos = Distrito.objects.filter(descricao__icontains=destinoget)

	municipios = Municipio.objects.all()
	'''id_destino = request.GET.get("id")
	distritos = Distrito.objects.get(id=id_destino)
	municipios = Municipio.objects.get(id=id_destino)'''

	if request.method == 'GET':
		if 'destinoget' in request.GET:
			destinoget=request.GET.get("destinoget")
		else:
			destinoget=""

		if 'destinoget' in request.GET and request.GET.get("destinoget")!="":
			destinoget=request.GET.get("destinoget")
		else:
			destinoget=Distrito.objects.values_list('id')
		distritos = Distrito.objects.filter(descricao__icontains=destinoget).distinct()
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
	
'''def avaliacoes(request):
	id_distrito = request.POST.get("id")
	nota = request.POST.get("nota")
	comentarios = request.POST.get("comentarios")

	#Consultar no banco o objeto distrito (linha 19 e linha 23)

	avaliacao = Avaliacao()
	avaliacao.nota = nota
	avaliacao.descricao = comentarios
	avaliacao.Distrito = distrito #objeto retornado

	avaliacao.save()

	return render(request, 'sucesso.html')'''

def sucesso(request):

	form2 = AvaliacaoModelForm(request.POST or None)
	context = {

		'form2': form2
	}

	if form2.is_valid():		
			avaliacao.save()



	return render(request, 'sucesso.html', context)

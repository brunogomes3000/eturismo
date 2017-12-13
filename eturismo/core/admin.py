from django.contrib import admin

# Register your models here.

from .models import Administrador
from .models import Tipo_Passeio
from .models import Empresa
from .models import Municipio
from .models import Distrito
from .models import Estado
from .models import Tipo_Filtro
from .models import Tipo_Dica
from .models import Dica
from .models import Promocao
from .models import Endereco
from .models import Tipo_Contato
from .models import Contato
from .models import Avaliacao

class AdministradorAdimin(admin.ModelAdmin):
	list_display = ['nome', 'cpf', 'login']
	search_fields = ['nome', 'cpf', 'login']

class EstadoAdimin(admin.ModelAdmin):
	list_display = ['descricao']
	search_fields = ['descricao']
	list_filter= ['descricao']

class MunicipioAdimin(admin.ModelAdmin):
	list_display = ['descricao', 'Estado']
	search_fields = ['descricao', 'Estado']
	list_filter= ['descricao', 'Estado']

class DistritoAdimin(admin.ModelAdmin):
	list_display = ['descricao', 'Municipio']
	search_fields = ['descricao', 'Municipio']
	list_filter= ['descricao', 'Municipio']

class PromocaoAdmin(admin.ModelAdmin):
	list_display = [ 'link', 'Empresa']
	search_fields = [ 'link', 'Empresa']
	list_filter = [ 'link', 'Empresa']

class AvaliacaoAdmin(admin.ModelAdmin):
	list_display = [ 'nota', 'descricao']
	search_fields = [ 'nota', 'descricao']
	list_filter= [ 'nota', 'descricao']

class PromocaoAdmin(admin.ModelAdmin):
	list_display = ['imagem', 'link', 'Empresa']
	search_fields = ['imagem', 'link', 'Empresa']
	list_filter = ['imagem', 'link', 'Empresa']



admin.site.register(Administrador, AdministradorAdimin)
admin.site.register(Tipo_Passeio)
admin.site.register(Empresa)
admin.site.register(Municipio, MunicipioAdimin)
admin.site.register(Estado, EstadoAdimin)
admin.site.register(Distrito, DistritoAdimin)
admin.site.register(Tipo_Dica)
admin.site.register(Tipo_Filtro)
admin.site.register(Dica)
admin.site.register(Promocao, PromocaoAdmin)
admin.site.register(Endereco)
admin.site.register(Tipo_Contato)
admin.site.register(Contato)
admin.site.register(Avaliacao, AvaliacaoAdmin)


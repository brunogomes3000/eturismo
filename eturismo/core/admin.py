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

class AdministradorAdimin(admin.ModelAdmin):
	list_display = ['nome', 'login']
	search_fields = ['nome', 'login']
	list_filter = ['Administrador']

admin.site.register(Administrador, AdministradorAdimin)
admin.site.register(Tipo_Passeio)
admin.site.register(Empresa)
admin.site.register(Municipio)
admin.site.register(Estado)
admin.site.register(Distrito)
admin.site.register(Tipo_Dica)
admin.site.register(Tipo_Filtro)
admin.site.register(Dica)
admin.site.register(Promocao)
admin.site.register(Endereco)
admin.site.register(Tipo_Contato)
admin.site.register(Contato)

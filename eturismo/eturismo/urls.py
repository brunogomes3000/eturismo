"""eturismo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import index
from core.views import informacoes
from core.views import lista_destinos
from core.views import passeio_detalhes
from core.views import sucesso
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^$', index, name="index"),
	url(r'^informacoes', informacoes, name="informacoes" ), 
    url(r'^lista_destinos',lista_destinos, name="lista_destinos"),
    url(r'^sucesso',sucesso, name="sucesso"),
    url(r'^passeio_detalhes',passeio_detalhes, name="passeio_detalhes"),   
    url(r'^admin/', admin.site.urls),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

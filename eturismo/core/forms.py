from django import forms
from django.forms import ModelForm
from .models import Avaliacao

class AvaliacaoModelForm(forms.ModelForm):	
	class Meta:
		model = Avaliacao
		fields = ['nota','descricao']
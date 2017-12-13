from django.db import models

# Create your models here.
class Usuario(models.Model):
	nome = models.CharField('Nome', max_length=100)
	cpf = models.CharField('CPF', max_length=11)
	def __str__(self):
		return self.nome

	

class Administrador(models.Model):
	cpf = models.CharField('CPF', primary_key=True, max_length=11)
	nome = models.CharField('Nome', max_length=100)
	login = models.CharField('Login', max_length=30)
	imagem_perfil = models.ImageField(upload_to='imagens/perfil', verbose_name='Imagem', default='imagens/perfil/noperfil.png', null=True, blank=True)

	def __str__(self):
		return self.login

	class Meta:
		ordering = ['nome']


class Tipo_Passeio(models.Model):
	descricao = models.CharField('Descricao', max_length=200)
	def __str__(self):
		return self.descricao

class Empresa(models.Model):
	cnpj = models.CharField('CNPJ', max_length=7)
	descricao = models.CharField('Descrição', max_length=30)
	site = models.CharField('Site', max_length=40)
	def __str__(self):
		return self.descricao

class Estado(models.Model):
	descricao = models.CharField("Descricao", max_length=100)
	def __str__(self):
		return self.descricao

class Municipio(models.Model):
	descricao = models.CharField("Descricao", max_length=100)
	Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	def __str__(self):
		return self.descricao

class Distrito(models.Model):
	descricao = models.CharField("Descricao", max_length=100)
	Municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	def __str__(self):
		return self.descricao

class Tipo_Filtro(models.Model):
	descricao = models.CharField("Descricao", max_length=1000)
	def __str__(self):
		return self.descricao

class Tipo_Dica(models.Model):
	descricao = models.CharField("Descricao", max_length=1000)
	Tipo_Filtro = models.ForeignKey(Tipo_Filtro, on_delete=models.CASCADE)
	def __str__(self):
		return self.descricao

class Dica(models.Model):
	descricao = models.CharField("Descricao", max_length=500)
	Tipo_Dica = models.ForeignKey(Tipo_Dica, on_delete=models.CASCADE)
	Distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
	def __str__(self):
		return self.descricao


class Passeio(models.Model):
	localizacao = models.CharField('Localização', max_length=250)
	descricao = models.CharField("Descrição", max_length=500)
	Tipo_Passeio = models.ForeignKey(Tipo_Passeio, on_delete=models.CASCADE)
	Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	Municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
	def __str__(self):
		return self.descricao

class Promocao(models.Model):
	imagem_perfil= models.ImageField(upload_to='imagens/perfil', verbose_name='Imagem', default='imagens/perfil/noperfil.png', null=True, blank=True)
	link = models.CharField("Link", max_length=100)
	Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	def __str__(self):
		return self.link

class Endereco(models.Model):
	cep= models.CharField("CEP", max_length=12)
	logradouro = models.CharField("Logradouro", max_length=50)
	nome=models.CharField("Nome", max_length=50)
	numero=models.CharField("Número", max_length=50)
	lat=models.DecimalField("Latitude", max_digits=7, decimal_places=6)
	log=models.DecimalField("Longitude",max_digits=7, decimal_places=6)
	def __str__(self):
		return self.nome

class Tipo_Contato(models.Model):
	descricao = models.CharField('Descrição', max_length=30)
	def __str__(self):
		return self.descricao	

class Contato(models.Model):
	descricao = models.CharField('Descrição', max_length=30)
	Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)	
	Tipo_Contato = models.ForeignKey(Tipo_Contato, on_delete=models.CASCADE)	
	def __str__(self):
		return self.descricao

class Avaliacao(models.Model):
	nota = models.CharField('Nota', max_length=2)
	descricao = models.CharField('Descrição', max_length=300)
	def __str__(self):
		return self.nota
		
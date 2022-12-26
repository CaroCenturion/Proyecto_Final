from django.db import models
from apps.usuarios.models import Usuario

class Posteo(models.Model):

	titulo = models.CharField(max_length = 150)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'post')
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.titulo
class Comentar_post(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	posteos = models.ForeignKey(Posteo, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{posteos}->{texto}"
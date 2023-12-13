from django.db import models
from django.contrib.auth.models import User


class Projecto(models.Model):
    
    autor = modes.models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField('nome', max_length=100, null=False)
    descricao = models.TextField('descriçao', null=False)
    imagem = models.ImageField(null=False, upload_to='prototipos')
    data = models.DateTimeField(auto_now_add=True)
    data_up = models.DateTimeField(auto_now=True)
    url_proj = models.CharField('url do projecto em prod', max_length=200)
    
    
    def __str__(self):
        return self.nome
from django.db import models
from django.contrib.auth.models import User



class Servico(models.Model):
    
    imagem = models.ImageField(upload_to='icones-servicos')
    servico = models.CharField('serviço', null=False, max_length=100)
    descricao = models.TextField('descriçao', null=False)
    
    def __str__(self):
        return self.servico

class Habilidade(models.Model):
    ferramenta = models.CharField('ferramenta', null=False, unique=True, max_length=100 )
    percentagem = models.IntegerField(null=False)
    
    def __str__(self):
        return self.ferramenta
    
    
class Projecto(models.Model):
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField('nome', max_length=100, null=False)
    descricao = models.TextField('descriçao', null=False)
    imagem = models.ImageField(null=False, upload_to='prototipos', default='default.jpg')
    data = models.DateTimeField(auto_now_add=True)
    data_up = models.DateTimeField(auto_now=True)
    url_proj = models.CharField('url do projecto em prod', max_length=200)
    
    
    def __str__(self):
        return self.nome
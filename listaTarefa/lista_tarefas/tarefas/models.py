from django.db import models

class Tarefa(models.Model):
    descricao = models.TextField()
    status = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao
    

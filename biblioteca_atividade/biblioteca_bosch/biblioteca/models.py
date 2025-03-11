from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Meta:
        verbose_name_plural = "Livros"
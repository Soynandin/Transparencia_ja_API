from django.db import models

class Contratantes(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome

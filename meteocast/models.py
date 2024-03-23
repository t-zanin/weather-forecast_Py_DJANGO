# Importe o módulo models do Django
from django.db import models

# Defina o modelo PrevisaoTempo
class PrevisaoTempo(models.Model):
    # Campos do modelo
    data = models.DateField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    umidade = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=100)

    # Método para representação textual do objeto
    def __str__(self):
        return f'Previsão do Tempo em {self.data}'


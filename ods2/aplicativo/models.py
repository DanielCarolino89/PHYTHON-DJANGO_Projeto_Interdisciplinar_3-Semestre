from djongo import models

class odsModels(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        abstract = True
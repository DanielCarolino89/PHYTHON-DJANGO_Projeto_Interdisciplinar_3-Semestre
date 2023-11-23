from djongo import models

class PessoaFisica(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=10)
    orgao = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    sobre = models.TextField(max_length=200)
    encontrou = models.CharField(max_length=20)
    declaracao = models.CharField(max_length=200)

    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.cpf, self.nome)

class PessoaJuridica(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=14)
    empresa = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    cargo = models.CharField(max_length=50)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    sobre = models.TextField(max_length=200)
    encontrou = models.CharField(max_length=20)
    declaracao = models.CharField(max_length=200)


    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.cnpj, self.empresa)

class PessoaApoio(models.Model):
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=10)
    orgao = models.CharField(max_length=50)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    pessoas = models.IntegerField()
    sobre = models.TextField(max_length=200)
    encontrou = models.CharField(max_length=20)
    declaracao = models.CharField(max_length=200)

    modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{} ({})".format(self.cpf, self.nome)
    
class ItemsDoacao(models.Model):
        dia = models.CharField(max_length=8)
        item = models.CharField(max_length=128)
        quantidade = models.IntegerField()
        peso = models.DecimalField(max_digits=10, decimal_places=2)
        validade = models.DateField()

        modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

        def __str__(self):
            return "{} ({})".format(self.item, self.validade)    
from django import forms
from aplicativo.models import apoioModels, cnpjModels, cpfModels

class cpfForm(forms.ModelForm):
    class Meta:
        model = cpfModels
        fields = ['usuario','senha','cpf','rg','orgao','nome','idade','endereco','numero','bairro','cidade','estado','telefone','celular','sobre','encontrou','declaracao']

class cnpjForm(forms.ModelForm):
    class Meta:
        model = cnpjModels
        fields = fields = ['usuario','senha','cnpj','empresa','responsavel','cargo','endereco','numero','bairro','cidade','estado','telefone','celular','sobre','encontrou','declaracao']

class apoioForm(forms.ModelForm):
    class Meta:
        model = apoioModels
        fields = ['cpf','rg','orgao','nome','idade','endereco','numero','bairro','cidade','estado','telefone','celular','renda','pessoas','sobre','encontrou','declaracao']

         
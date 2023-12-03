from django.test import TestCase
from django.urls import reverse
from pymongo import MongoClient
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from aplicativo.models import ItemsDoacao
from aplicativo.services.ConexaoMongoDB import CRUD_PessoaCadastro, ConexaoDATABASE

class IndexTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('')

    #Este erro indica que o recurso que você está tentando acessar não foi encontrado.
    def test_200(self):
        self.assertEqual(200, self.resp.status_code)
    
class PFsalvarViewTest(TestCase):
    def test_PFsalvar_view(self):

        user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        User.objects.create_user(**user_data)

        post_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
        }
        response = self.client.post(reverse('pfsalvar'), post_data)
        self.assertEqual(User.objects.filter(username='newuser').count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        User.objects.get(username='newuser').delete()

class PessoaCadastroViewTest(TestCase):
    def main():
    
        connection = ConexaoDATABASE()
        crud_instance = CRUD_PessoaCadastro(connection)
        crud_instance.insert(cpf="37525800899", rg="462454211")
        documents = crud_instance.view(cpf="37525800899")
        for document in documents:
            print(document)

    if __name__ == "__main__":
        main()

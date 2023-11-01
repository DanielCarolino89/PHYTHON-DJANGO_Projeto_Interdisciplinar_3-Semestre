from operator import index
from unittest import TestCase
from unittest.mock import patch
from aplicativo.forms import odsForm
from aplicativo.services.MongoConnection import MongoConnection
from .views import apoio, cadastro, junte, parceiros, sobre

class CadastroTest(TestCase):

    def test_post_request_with_valid_form(self):
        # """Testa que uma requisição POST com um formulário válido cadastra o usuário no MongoDB."""

        # Cria um formulário válido
        form = odsForm({'nome': 'John Doe'})
        form.is_valid()

        # Mocka a conexão com o MongoDB
        with patch.object(MongoConnection, '__init__', lambda self: None):
            # Faz a requisição POST
            response = cadastro(self.client, method='POST', data=form)

            # Verifica se a resposta é um redirect para a página `junte.html`
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, '/junte/')

    def test_post_request_with_invalid_form(self):
        # """Testa que uma requisição POST com um formulário inválido retorna um erro."""

        # Cria um formulário inválido
        form = odsForm({'nome': ''})
        form.is_valid()

        # Faz a requisição POST
        response = cadastro(self.client, method='POST', data=form)

        # Verifica se a resposta é um erro 400
        self.assertEqual(response.status_code, 400)

        # Verifica se a mensagem de erro contém o motivo da invalidação do formulário
        self.assertIn('Este campo é obrigatório.', response.content)

    def test_get_request(self):
        # """Testa que uma requisição GET retorna a página `junte.html` com um formulário vazio."""

        # Faz a requisição GET
        response = cadastro(self.client, method='GET')

        # Verifica se a resposta é a página `junte.html`
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'junte.html')

        # Verifica se o formulário no contexto da resposta está vazio
        self.assertEqual(response.context['form'].is_bound, False)

class ViewsTest(TestCase):

    def test_index_view(self):
        # """Testa que a view `index()` retorna a página `index.html`."""

        response = index(self.client)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'index.html')

    def test_junte_view(self):
        # """Testa que a view `junte()` retorna a página `junte.html`."""

        response = junte(self.client)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'junte.html')

    def test_apoio_view(self):
        # """Testa que a view `apoio()` retorna a página `apoio.html`."""

        response = apoio(self.client)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'apoio.html')

    def test_parceiros_view(self):
        # """Testa que a view `parceiros()` retorna a página `parceiros.html`."""

        response = parceiros(self.client)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'parceiros.html')

    def test_sobre_view(self):
        # """Testa que a view `sobre()` retorna a página `sobre.html`."""

        response = sobre(self.client)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'sobre.html')

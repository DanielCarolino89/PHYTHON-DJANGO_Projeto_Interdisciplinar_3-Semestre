import unittest
from unittest.mock import MagicMock
from django.forms import FilePathField
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from aplicativo.services.ConexaoMongoDB import CRUD_PessoaApoio, CRUD_PessoaCadastro, ConexaoDATABASE, Consultas



class ViewsTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_junte_view(self):
        response = self.client.get(reverse('junte'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'junte.html')

    def test_apoio_view(self):
        response = self.client.get(reverse('apoio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'apoio.html')

    def test_parceiros_view(self):
        response = self.client.get(reverse('parceiros'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'parceiros.html')

    def test_sobre_view(self):
        response = self.client.get(reverse('sobre'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sobre.html')

    def test_cadastro_pf_view(self):
        response = self.client.get(reverse('cadastro_pf'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro_pf.html')

    def test_cadastro_pj_view(self):
        response = self.client.get(reverse('cadastro_pj'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro_pj.html')

class ConexaoDATABASETesT(TestCase):
    def test_get_connection(self):
        # Crie uma instância da classe ConexaoDATABASE
        conexao = ConexaoDATABASE()

        # Chame o método getConnection() e verifique se a conexão é bem-sucedida
        try:
            connection = conexao.getConnection()
            self.assertTrue(connection.server_info())  # Verifica se a conexão foi bem-sucedida
        except Exception as e:
            self.fail(f"A conexão falhou com o seguinte erro: {str(e)}")

class UsuarioEditarViewTest(TestCase):
    def setUp(self):
        # Crie um usuário para ser editado
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        # Crie um cliente para simular solicitações
        self.client = Client()

        # Defina a URL da view de edição do usuário
        self.url = reverse('usuario_editar', args=[self.user.id])

    def test_usuario_editar_view(self):
        # Faça login antes de chamar a view de edição (caso necessário)
        self.client.login(username='testuser', password='testpassword')

        # Dados para a solicitação POST
        new_username = 'new_testuser'
        new_email = 'new_test@example.com'
        new_password = 'new_testpassword'

        # Simule uma solicitação POST para a view de edição do usuário
        response = self.client.post(self.url, {'username': new_username, 'email': new_email, 'password': new_password})

        # Verifique se a resposta redireciona para a página de logout
        self.assertRedirects(response, reverse('logout'))

        # Recarregue o usuário do banco de dados
        updated_user = get_user_model().objects.get(id=self.user.id)

        # Verifique se os dados do usuário foram atualizados corretamente
        self.assertEqual(updated_user.username, new_username)
        self.assertEqual(updated_user.email, new_email)
        self.assertTrue(updated_user.check_password(new_password))

class ApoiosalvarViewTest(TestCase):
    def setUp(self):
        # Crie um cliente para simular as solicitações
        self.client = Client()

class CRUD_PessoaCadastroTest(unittest.TestCase):
    def setUp(self):
        # Crie um objeto de conexão fictício para os testes
        self.connection_mock = MagicMock()

        # Crie uma instância da classe CRUD_PessoaCadastro para cada teste
        self.crud_instance = CRUD_PessoaCadastro(self.connection_mock)

    def test_insert(self):
        # Configurar dados fictícios para a inserção
        data = {'name': 'John Doe', 'age': 25}

        # Chamar o método insert
        self.crud_instance.insert(**data)

        # Verificar se o método insert_one foi chamado no objeto de coleção
        self.crud_instance.db['cd_PessoaCadastro'].insert_one.assert_called_once_with(data)

    def test_delete(self):
        # Configurar dados fictícios para a exclusão
        query = {'name': 'John Doe'}

        # Chamar o método delete
        self.crud_instance.delete(**query)

        # Verificar se o método delete_one foi chamado no objeto de coleção
        self.crud_instance.db['cd_PessoaCadastro'].delete_one.assert_called_once_with(query)

    def test_update(self):
        # Configurar dados fictícios para a atualização
        update_data = {'age': 26}
        query = {'name': 'John Doe'}

        # Chamar o método update
        self.crud_instance.update(_id=1, **update_data)

        # Verificar se o método update_one foi chamado no objeto de coleção
        self.crud_instance.db['cd_PessoaCadastro'].update_one.assert_called_once_with({'_id': 1}, {"$set": update_data})

    def test_view(self):
        # Configurar dados fictícios para a visualização
        query = {'name': 'John Doe'}

        # Chamar o método view
        self.crud_instance.view(**query)

        # Verificar se o método find foi chamado no objeto de coleção
        self.crud_instance.db['cd_PessoaCadastro'].find.assert_called_once_with(query) 

class ConsultasTest(unittest.TestCase):
    def setUp(self):
        # Crie um objeto de conexão fictício para os testes
        self.connection_mock = MagicMock()

        # Crie uma instância da classe Consultas para cada teste
        self.consultas_instance = Consultas(self.connection_mock)

    def test_total_doacoes(self):
        # Configurar um objeto de coleção fictício para o teste
        collection_mock = MagicMock()
        collection_mock.count_documents.return_value = 42

        # Substituir o objeto de coleção real pelo objeto fictício no objeto Consultas
        self.consultas_instance.db['cd_ItemsDoacao'] = collection_mock

        

    def test_doacoes_por_item(self):
        # Configurar um objeto de coleção fictício para o teste
        collection_mock = MagicMock()
        collection_mock.count_documents.return_value = 10

        # Substituir o objeto de coleção real pelo objeto fictício no objeto Consultas
        self.consultas_instance.db['cd_ItemsDoacao'] = collection_mock

        

    def test_quantidade_total_por_item(self):
        # Configurar um objeto de cursor fictício para o teste
        cursor_mock = MagicMock()
        cursor_mock.__iter__.return_value = [{'_id': {'item': 'Livro'}, 'totalQuantidade': 25}]

        # Substituir a chamada real para aggregate com o objeto fictício no objeto Consultas
        self.consultas_instance.db['cd_ItemsDoacao'].aggregate.return_value = cursor_mock

    
    def test_valor_medio_total(self):
        # Configurar um objeto de coleção fictício para o teste
        collection_mock = MagicMock()
        collection_mock.count_documents.return_value = 100

        # Substituir o objeto de coleção real pelo objeto fictício no objeto Consultas
        self.consultas_instance.db['cd_ItemsDoacao'] = collection_mock

class ApoiosalvarViewTest(TestCase):
    def setUp(self):
        # Crie um cliente para simular as solicitações
        self.client = Client()

    def test_apoiosalvar_view(self):
        # Dados fictícios para a solicitação POST
        data = {
            'cpf': '37525800899',
            'rg': '12345',
            'orgao': 'SSP',
            'nome': 'John Doe',
            'idade': '30',
            'endereco': 'Rua Teste',
            'numero': '42',
            'bairro': 'Centro',
            'cidade': 'Cidade Teste',
            'estado': 'TS',
            'telefone': '123456789',
            'celular': '987654321',
            'renda': '1000.00',
            'pessoas': '3',
            'sobre': 'Sobre o pedido',
            'encontrou': 'Internet',
            'declaracao': 'Concordo com os termos',
        }

        # Simule uma solicitação POST para a view
        self.client.post('/Apoiosalvar/', data)

        # Verifique se os dados foram inseridos corretamente no MongoDB (ou outro banco de dados usado)
        conexao = ConexaoDATABASE()
        colecao = CRUD_PessoaApoio(conexao)


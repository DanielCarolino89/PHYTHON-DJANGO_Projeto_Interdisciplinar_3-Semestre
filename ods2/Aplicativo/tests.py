from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskListTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title="Tarefa 1")
        Task.objects.create(title="Tarefa 2")

    def test_task_list_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) 
        # indica que a página foi carregada com sucesso.

    def test_task_list_view_template(self):
        response = self.client.get(reverse('task_list'))
        self.assertTemplateUsed(response, 'tasks/task_list.html') 
        # verifica se a view está usando o modelo de template correto

    def test_task_list_view_contains_tasks(self):
        response = self.client.get(reverse('task_list'))
        self.assertContains(response, 'Tarefa 1')
        self.assertContains(response, 'Tarefa 2')
        #verifica se a lista de tarefas exibe as tarefas que criamos no método setUp

      

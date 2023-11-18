from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('junte', views.junte, name='junte'),
    path('apoio', views.apoio, name='apoio'),
    path('parceiros', views.parceiros, name='parceiros'),
    path('sobre', views.sobre, name='sobre'),
    path('cpf', views.cpf, name='cpf'),
    path('cnpj', views.cnpj, name='cnpj'),
    path('CadastroApoio',views.CadastroApoio, name='CadastroApoio'),
    path('CadastroCNPJ',views.CadastroCNPJ, name='CadastroCNPJ'),
    path('CadastroCPF',views.CadastroCPF, name='CadastroCPF'),
    path('base',views.base, name='base'),
]
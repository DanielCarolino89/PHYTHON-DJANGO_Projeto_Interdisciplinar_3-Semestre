from django.urls import path, include
from aplicativo import views

urlpatterns = [
    path('',views.index,name='index'),
    path('junte',views.junte,name='junte'),
    path('apoio',views.apoio,name='apoio'),
    path('parceiros',views.parceiros,name='parceiros'),
    path('sobre',views.sobre,name='sobre'),
    path('cadastro_pf',views.cadastro_pf,name='cadastro_pf'),
    path('cadastro_pj',views.cadastro_pj,name='cadastro_pj'),

    path('pfsalvar',views.PFsalvar,name='pfsalvar'),
    path('editar/<int:id>',views.PFeditar,name='editar'),
    path('update/<int:id>',views.PFupdate,name='update'),
    path('delete/<int:id>',views.PFdelete,name='delete'),

    path('pjsalvar',views.PJsalvar,name='pjsalvar'),
    path('editar/<int:id>',views.PJeditar,name='editar'),
    path('update/<int:id>',views.PJupdate,name='update'),
    path('delete/<int:id>',views.PJdelete,name='delete'),

    path('dcsalvar',views.DCsalvar,name='dcsalvar'),
    path('editar/<int:id>',views.DCeditar,name='editar'),
    path('update/<int:id>',views.DCupdate,name='update'),
    path('delete/<int:id>',views.DCdelete,name='delete'),
   
    path('apoiosalvar',views.Apoiosalvar,name='apoiosalvar'),

    path('botao',views.botao, name='botao'),
    path('login',views.login_view, name='login'),
    path('logout',views.logout_view,name='logout'),

    path('usuario_index',views.usuario_index,name='usuario_index'),
    path('usuario_cad_doacao',views.usuario_cad_doacao,name='usuario_cad_doacao'),
    path('usuario_relatorios',views.DCvisualizar,name='usuario_relatorios'),
    path('usuario_att_dados',views.usuario_att_dados,name='usuario_att_dados'),

    
   
    
    
]


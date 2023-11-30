from django.urls import path, include
from aplicativo import views

urlpatterns = [
    path('',views.index,name='index'),#OK
    path('junte',views.junte,name='junte'),#OK
    path('apoio',views.apoio,name='apoio'),#OK
    path('parceiros',views.parceiros,name='parceiros'),#OK
    path('sobre',views.sobre,name='sobre'),#OK
    path('cadastro_pf',views.cadastro_pf,name='cadastro_pf'),#OK
    path('cadastro_pj',views.cadastro_pj,name='cadastro_pj'),#OK

    path('pfsalvar',views.PFsalvar,name='pfsalvar'),#OK
    path('editar/<int:id>',views.PFeditar,name='editar'),
    path('update/<int:id>',views.PFupdate,name='update'),
    path('delete/<int:id>',views.PFdelete,name='delete'),

    path('pjsalvar',views.PJsalvar,name='pjsalvar'),
    path('editar/<int:id>',views.PJeditar,name='editar'),
    path('update/<int:id>',views.PJupdate,name='update'),
    path('delete/<int:id>',views.PJdelete,name='delete'),

    path('dcsalvar',views.DCsalvar,name='dcsalvar'),#OK
    path('doacao_editar/<int:id>',views.DCeditar,name='doacao_editar'),#OK
    path('doacao_update/<int:id>',views.DCupdate,name='doacao_update'),#OK
    path('dcdelete/<int:id>',views.DCdelete,name='dcdelete'),#OK
    path('doacao_index',views.DCvisualizar,name='doacao_index'),#OK
   
    path('apoiosalvar',views.Apoiosalvar,name='apoiosalvar'),#OK

    path('botao',views.botao, name='botao'), #OK
    path('login',views.login_view, name='login'),#OK
    path('logout',views.logout_view,name='logout'),#OK

    path('doacao_info',views.doacao_info,name='doacao_info'),
    path('doacao_suporte',views.doacao_suporte,name='doacao_suporte'),
    path('doacao_relatorio',views.doacao_relatorio,name='doacao_relatorio'),
    
 
]


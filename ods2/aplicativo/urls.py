from django.urls import path, include
from .views import Apoiosalvar, DCdelete, DCeditar, DCsalvar, DCupdate, DCvisualizar, Login, Logout, PJdelete, PJeditar, PJsalvar, PJupdate, apoio, cadastro_pf, cadastro_pj, index,PFsalvar,PFeditar,PFupdate,PFdelete, junte, parceiros, sobre, usuario_att_dados, usuario_cad_doacao, usuario_index, usuario_relatorios

urlpatterns = [
    path('',index,name='index'),
    path('junte',junte,name='junte'),
    path('apoio',apoio,name='apoio'),
    path('parceiros',parceiros,name='parceiros'),
    path('sobre',sobre,name='sobre'),
    path('cadastro_pf',cadastro_pf,name='cadastro_pf'),
    path('cadastro_pj',cadastro_pj,name='cadastro_pj'),

    path('pfsalvar',PFsalvar,name='pfsalvar'),
    path('editar/<int:id>',PFeditar,name='editar'),
    path('update/<int:id>',PFupdate,name='update'),
    path('delete/<int:id>',PFdelete,name='delete'),

    path('pjsalvar',PJsalvar,name='pjsalvar'),
    path('editar/<int:id>',PJeditar,name='editar'),
    path('update/<int:id>',PJupdate,name='update'),
    path('delete/<int:id>',PJdelete,name='delete'),

    path('dcsalvar',DCsalvar,name='dcsalvar'),
    path('editar/<int:id>',DCeditar,name='editar'),
    path('update/<int:id>',DCupdate,name='update'),
    path('delete/<int:id>',DCdelete,name='delete'),
   
    path('apoiosalvar',Apoiosalvar,name='apoiosalvar'),

    path('login',Login,name='login'),
    path('logout',Logout,name='logout'),

    path('usuario_index',usuario_index,name='usuario_index'),
    path('usuario_cad_doacao',usuario_cad_doacao,name='usuario_cad_doacao'),
    path('usuario_relatorios',DCvisualizar,name='usuario_relatorios'),
    path('usuario_att_dados',usuario_att_dados,name='usuario_att_dados'),
    
]


from django.contrib import admin

from aplicativo.models import PessoaCadastro,PessoaApoio,ItemsDoacao

admin.site.register(PessoaCadastro),
admin.site.register(PessoaApoio),
admin.site.register(ItemsDoacao),
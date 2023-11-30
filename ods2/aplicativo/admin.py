from django.contrib import admin

from aplicativo.models import PessoaFisica,PessoaJuridica,PessoaApoio,ItemsDoacao

admin.site.register(PessoaFisica),
admin.site.register(PessoaJuridica),
admin.site.register(PessoaApoio),
admin.site.register(ItemsDoacao),
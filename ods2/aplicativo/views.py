from django.http import HttpResponse
from django.shortcuts import render
from aplicativo.forms import odsForm
from .services.ConexaoMongoDatabase  import ConexaoBD

def cadastro(request):
    if request.method == 'POST':
        form = odsForm(request.POST)
        if form.is_valid():
            try:

                nome = form.clean_nome()
            
            except Exception as e:
                return HttpResponse(f'Erro: {str(e)}')

            conexao = ConexaoBD()
            client = ConexaoBD(conexao)
            client.insert(nome = nome)
            
            return render(request, 'junte.html',{'form':odsForm()})

    else:
        return render(request, 'junte.html',{'form':odsForm()})

def index(request):
    return render(request, 'index.html')

def junte(request):
    return render(request, 'junte.html')

def apoio(request):
    return render(request, 'apoio.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def sobre(request):
    return render(request, 'sobre.html')
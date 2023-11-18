from django.http import HttpResponse
from django.shortcuts import redirect, render
from aplicativo.forms import apoioForm, cnpjForm, cpfForm
from aplicativo.services.ConexaoMongoDB import ConexaoAPOIO, ConexaoCNPJ, ConexaoCPF, ConexaoDATABASE


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

def cpf(request):
    return render(request, 'cpf.html')

def cnpj(request):
    return render(request, 'cnpj.html')

def base(request):
    return render(request, 'base.html')
    
def CadastroCPF(request):
    if request.method == 'POST':
        form = cpfForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            senha = form.data['senha']
            cpf = form.data['cpf']
            rg = form.data['rg']
            orgao = form.data['orgao']
            nome = form.data['nome']
            idade = form.data['idade']
            endereco = form.data['endereco']
            numero = form.data['numero']
            bairro = form.data['bairro']
            cidade = form.data['cidade']
            estado = form.data['estado']
            telefone = form.data['telefone']
            celular = form.data['celular']
            sobre = form.data['sobre']
            encontrou = form.data['encontrou']
            declaracao = form.data['declaracao']
                    
            conexao = ConexaoDATABASE()
            colecao = ConexaoCPF(conexao)
            colecao.insert(email = email,senha = senha,cpf = cpf,rg = rg,orgao = orgao,nome = nome,idade = idade,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,sobre = sobre,encontrou = encontrou,declaracao = declaracao)

            form.save()

        return redirect('sobre')

    else:
        form = apoioForm
        return render(request, 'index.html', {'form': form})
    
def CadastroCNPJ(request):
    if request.method == 'POST':
        form = cnpjForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            senha = form.data['senha']
            cnpj = form.data['cnpj']
            empresa = form.data['empresa']
            responsavel = form.data['responsavel']
            cargo = form.data['cargo']
            endereco = form.data['endereco']
            numero = form.data['numero']
            bairro = form.data['bairro']
            cidade = form.data['cidade']
            estado = form.data['estado']
            telefone = form.data['telefone']
            celular = form.data['celular']
            sobre = form.data['sobre']
            encontrou = form.data['encontrou']
            declaracao = form.data['declaracao']

            conexao = ConexaoDATABASE()
            colecao = ConexaoCNPJ(conexao)
            colecao.insert(email = email,senha = senha,cnpj = cnpj,empresa = empresa,responsavel = responsavel,cargo = cargo,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,sobre = sobre,encontrou = encontrou,declaracao=declaracao)

            form.save()

        return redirect('sobre')

    else:
        form = cnpjForm
        return render(request, 'index.html', {'form': form})

def CadastroApoio(request):
    if request.method == 'POST':
        form = apoioForm(request.POST)
        if form.is_valid():
            cpf = form.data['cpf']
            rg = form.data['rg']
            orgao = form.data['orgao']
            nome = form.data['nome']
            idade = form.data['idade']
            endereco = form.data['endereco']
            numero = form.data['numero']
            bairro = form.data['bairro']
            cidade = form.data['cidade']
            estado = form.data['estado']
            telefone = form.data['telefone']
            celular = form.data['celular']
            renda = form.data['renda']
            pessoas = form.data['pessoas']
            sobre = form.data['sobre']
            encontrou = form.data['encontrou']
            declaracao = form.data['declaracao']
                    
            conexao = ConexaoDATABASE()
            colecao = ConexaoAPOIO(conexao)
            colecao.insert(cpf = cpf,rg = rg,orgao = orgao,nome = nome,idade = idade,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,renda = renda,pessoas = pessoas,sobre = sobre,encontrou = encontrou,declaracao = declaracao)

            form.save()

        return redirect('sobre')

    else:
        form = apoioForm
        return render(request, 'index.html', {'form': form})





import datetime
from aplicativo.models import ItemsDoacao, PessoaApoio, PessoaFisica, PessoaJuridica
from aplicativo.services.ConexaoMongoDB import CRUD_ItemsDoacao, CRUD_PessoaApoio, CRUD_PessoaFisica, CRUD_PessoaJuridica, ConexaoDATABASE, Consultas, Find_Login

from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Começo Renders
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
def cadastro_pf(request):
    return render(request, 'cadastro_pf.html')
def cadastro_pj(request):
    return render(request, 'cadastro_pj.html')

# Começo PessoaFisica
def PFvisualizar(request):
    pessoas = PessoaFisica.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})

def PFsalvar(request):
    if request.method == "GET":
        return render(request, 'junte.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
    cpf = request.POST.get("cpf")
    rg = request.POST.get("rg")
    orgao = request.POST.get("orgao")
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    endereco = request.POST.get("endereco")
    numero = request.POST.get("numero")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    estado = request.POST.get("estado")
    telefone = request.POST.get("telefone")
    celular = request.POST.get("celular")
    sobre = request.POST.get("sobre")
    encontrou = request.POST.get("encontrou")
    declaracao = request.POST.get("declaracao")

    user = User.objects.filter(username=username).first()
    if user:
            return HttpResponse('<h2> Já exite um usuário com este username </h2>') 
    
    user = User.objects.create_user(username=username,password=password)
    user.save()

    PessoaFisica.objects.create(cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
                    numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
                    sobre=sobre,encontrou=encontrou,declaracao=declaracao)
    pessoas = PessoaFisica.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaFisica(conexao)
    colecao.insert(cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
                    numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
                    sobre=sobre,encontrou=encontrou,declaracao=declaracao)
        
    return render(request,"index.html", {"pessoas": pessoas})
   

def PFeditar(request,id):
    pessoas = PessoaFisica.objects.get(id=id)
    return render(request,"update.html", {"pessoas": pessoas})

def PFupdate(request,id):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    cpf = request.POST.get("cpf")
    rg = request.POST.get("rg")
    orgao = request.POST.get("orgao")
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    endereco = request.POST.get("endereco")
    numero = request.POST.get("numero")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    estado = request.POST.get("estado")
    telefone = request.POST.get("telefone")
    celular = request.POST.get("celular")
    sobre = request.POST.get("sobre")
    encontrou = request.POST.get("encontrou")
    declaracao = request.POST.get("declaracao")
    pessoas = PessoaFisica.objects.get(id=id)
    pessoas.email=email,senha=senha,cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
    numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
    sobre=sobre,encontrou=encontrou,declaracao=declaracao
    pessoas.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaFisica(conexao)
    colecao.update(email=email,senha=senha,cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
                   numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
                   sobre=sobre,encontrou=encontrou,declaracao=declaracao)

    return redirect('index')

def PFdelete(request,id):
    pessoas = PessoaFisica.objects.get(id=id)
    pessoas.delete()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaFisica(conexao)
    colecao.delete()

    return redirect('index') 
# Fim PessoaFisica

# Começo PessoaJuridica
def PJvisualizar(request):
    pessoas = PessoaJuridica.objects.all()
    return render(request,"index.html", {"pessoas": pessoas})

def PJsalvar(request):
    if request.method == "GET":
        return render(request, 'junte.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
    cnpj = request.POST.get("cnpj")
    empresa = request.POST.get("empresa")
    responsavel = request.POST.get("responsavel")
    cargo = request.POST.get("cargo")
    endereco = request.POST.get("endereco")
    numero = request.POST.get("numero")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    estado = request.POST.get("estado")
    telefone = request.POST.get("telefone")
    celular = request.POST.get("celular")
    sobre = request.POST.get("sobre")
    encontrou = request.POST.get("encontrou")
    declaracao = request.POST.get("declaracao")

    user = User.objects.filter(username=username).first()
    user = User.objects.create_user(username=username,password=password)#is_staff
    user.save()

    PessoaJuridica.objects.create(cnpj=cnpj,empresa=empresa,responsavel=responsavel,
                                  cargo=cargo,endereco=endereco,numero=numero,bairro=bairro,cidade=cidade,
                                  estado=estado,telefone=telefone,celular=celular,sobre=sobre,encontrou=encontrou,
                                  declaracao=declaracao)
    pessoas = PessoaJuridica.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaJuridica(conexao)
    colecao.insert(cnpj=cnpj,empresa=empresa,responsavel=responsavel,
                                  cargo=cargo,endereco=endereco,numero=numero,bairro=bairro,cidade=cidade,
                                  estado=estado,telefone=telefone,celular=celular,sobre=sobre,encontrou=encontrou,
                                  declaracao=declaracao)
    return render(request,"index.html", {"pessoas": pessoas})

def PJeditar(request,id):
    pessoas = PessoaJuridica.objects.get(id=id)
    return render(request,"update.html", {"pessoas": pessoas})

def PJupdate(request,id):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    cnpj = request.POST.get("cnpj")
    empresa = request.POST.get("empresa")
    responsavel = request.POST.get("responsavel")
    cargo = request.POST.get("cargo")
    endereco = request.POST.get("endereco")
    numero = request.POST.get("numero")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    estado = request.POST.get("estado")
    telefone = request.POST.get("telefone")
    celular = request.POST.get("celular")
    sobre = request.POST.get("sobre")
    encontrou = request.POST.get("encontrou")
    declaracao = request.POST.get("declaracao")
    pessoas = PessoaJuridica.objects.get(id=id)
    pessoas.email=email,senha=senha,cnpj=cnpj,empresa=empresa,responsavel=responsavel,cargo=cargo,endereco=endereco,numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,sobre=sobre,encontrou=encontrou,declaracao=declaracao
    pessoas.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaJuridica(conexao)
    colecao.update(email = email,senha = senha,cnpj = cnpj,empresa = empresa,responsavel = responsavel,cargo = cargo,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,sobre = sobre,encontrou = encontrou,declaracao=declaracao)

    return redirect('index')

def PJdelete(request,id):
    pessoas = PessoaJuridica.objects.get(id=id)
    pessoas.delete()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaJuridica(conexao)
    colecao.delete()

    return redirect('index')    
# Fim PessoaJuridica

# Começo doacoes
def DCvisualizar(request):
    doacoes = ItemsDoacao.objects.all()
    return render(request,"doacao_index.html", {"doacoes": doacoes})

def DCsalvar(request):
    item = request.POST.get("item")
    quantidade = request.POST.get("quantidade")
    medida = request.POST.get("medida")
    validade = request.POST.get("validade")

    ItemsDoacao.objects.create(item=item,quantidade=quantidade,medida=medida,validade=validade)
    doacoes = ItemsDoacao.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.insert(item=item,quantidade=quantidade,medida=medida,validade=validade)
    return render(request,"doacao_index.html", {"doacoes": doacoes})

def DCeditar(request,id):
    doacoes = ItemsDoacao.objects.get(id=id)
    return render(request,"doacao_editar.html", {"doacoes": doacoes})

def DCupdate(request,id):
    item = request.POST.get("item")
    quantidade = request.POST.get("quantidade")
    medida = request.POST.get("medida")
    validade = request.POST.get("validade")
    doacoes = ItemsDoacao.objects.get(id=id)
    doacoes.item=item,
    doacoes.quantidade=quantidade,
    doacoes.medida=medida,
    doacoes.validade=validade
    doacoes.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.update(item=item,quantidade=quantidade,medida=medida,validade=validade)

    return redirect('doacao_index') 

def DCdelete(request,id):
    doacoes = ItemsDoacao.objects.get(id=id)
    doacoes.delete()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.delete()

    return redirect('doacao_index')    
# Fim Doacoes

# Começo Apoio 
def Apoiosalvar(request):
    cpf = request.POST.get("cpf")
    rg = request.POST.get("rg")
    orgao = request.POST.get("orgao")
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    endereco = request.POST.get("endereco")
    numero = request.POST.get("numero")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    estado = request.POST.get("estado")
    telefone = request.POST.get("telefone")
    celular = request.POST.get("celular")
    renda = request.POST.get("renda")
    npessoas = request.POST.get("npessoas")
    sobre = request.POST.get("sobre")
    encontrou = request.POST.get("encontrou")
    declaracao = request.POST.get("declaracao")
    
    data = datetime.datetime.today().strftime("%d-%m-%Y")
    
    PessoaApoio.objects.create(cpf = cpf,rg = rg,orgao = orgao,nome = nome,idade = idade,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,renda = renda,npessoas = npessoas,sobre = sobre,encontrou = encontrou,declaracao = declaracao)
    pessoas = PessoaApoio.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaApoio(conexao)
    colecao.insert(cpf = cpf,rg = rg,orgao = orgao,nome = nome,idade = idade,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,renda = renda,pessoas = pessoas,sobre = sobre,encontrou = encontrou,declaracao = declaracao)
    
    with open("apoios.txt", "w") as f:

        f.write(f"{data}\t{cpf}\t{rg}\t{nome}\t{idade}\t{endereco}\t{numero}\t{bairro}\t{cidade}\t{estado}\t{telefone}\t{celular}\t{renda}\t{npessoas}\t{sobre}\t{encontrou}\t{declaracao}")
    return render(request,"index.html", {"pessoas": pessoas})
# Fim Apoio

# # Começo Login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['id'] = user.id #inicia seção (session)
            return render(request, 'doacao_index.html',{"id":id})
        else:
            return HttpResponse('<h1>ERRO - Digite Email e senha novamente ou cadastre para ter acesso</h1>')
    else:
        # Handle other HTTP methods as needed
        return HttpResponse('<h1>Method Not Allowed</h1>', status=405)
# # Fim Login

# Começo Logout
def logout_view(request):
   logout(request)
   return render(request, 'index.html')
# Fim Logout

# PARTE SISTEMA
def base2(request):
    pessoas = PessoaFisica.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})
   
def usuario_index(request):
    if request.user.is_authenticated:
        id = request.session.get('id')
    if id is not None:
        usuario = User.objects.filter(id=id)
        return render(request, "doacao_index.html", {"usuario": usuario})
    else:
        return HttpResponse('<h1>ACESSO NEGADO!!! - Informações da sessão não encontradas</h1>')


def botao(request):
    if request.user.is_authenticated:
        return render(request,"doacao_index.html")
    return render(request, 'junte.html')

def doacao_info(request):
    return render(request, 'doacao_info.html')

def doacao_suporte(request):
    return render(request, 'doacao_suporte.html')

def doacao_relatorio(request):
    item = request.POST.get("item")

    conexao = ConexaoDATABASE()
    consulta = Consultas(conexao)

    doacoes = ItemsDoacao.objects.all()
    total_doacoes = consulta.Total_doacoes()
    
    doacoes_por_item = consulta.doacoes_por_item(item)
    quantidade_total = consulta.quantidade_total_por_item(item)
    valor_medio = consulta.valor_medio_total()
    
    return render(request, 'doacao_relatorio.html', {"valor_medio":valor_medio,"doacoes": doacoes, 'total_doacoes': total_doacoes,'doacoes_por_item': doacoes_por_item, 'quantidade_total': quantidade_total})

import datetime
from aplicativo.models import ItemsDoacao, PessoaApoio, PessoaCadastro
from aplicativo.services.ConexaoMongoDB import CRUD_ItemsDoacao, CRUD_PessoaApoio, CRUD_PessoaCadastro, ConexaoDATABASE, Consultas

from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password

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

# Começo PessoaCadastro
def PFvisualizar(request):
    pessoas = PessoaCadastro.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})

def PFsalvar(request):
    if request.method == "GET":
        return render(request, 'junte.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
    cnpj = request.POST.get("cnpj")
    empresa = request.POST.get("empresa")
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
    user = User.objects.create_user(username=username,email=email,password=password)
    user.save()

    PessoaCadastro.objects.create(cnpj=cnpj,empresa=empresa,cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
                    numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
                    sobre=sobre,encontrou=encontrou,declaracao=declaracao)
    pessoas = PessoaCadastro.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaCadastro(conexao)
    colecao.insert(cnpj=cnpj,empresa=empresa,cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
                    numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
                    sobre=sobre,encontrou=encontrou,declaracao=declaracao,username=username,email=email,password=password)
        
    return render(request,"index.html", {"pessoas": pessoas,})
   
def PFeditar(request,id):
    pessoas = PessoaCadastro.objects.get(id=id)
    return render(request,"pfupdate.html", {"pessoas": pessoas})

def PFupdate(request, id):
    nome = request.POST.get("nome")
    endereco = request.POST.get("endereco")
    numero = request.POST.get("numero")
    bairro = request.POST.get("bairro")
    cidade = request.POST.get("cidade")
    estado = request.POST.get("estado")
    telefone = request.POST.get("telefone")
    celular = request.POST.get("celular")

    pessoa = PessoaCadastro.objects.get(id=id)
    pessoa.nome = nome
    pessoa.endereco = endereco
    pessoa.numero = numero
    pessoa.bairro = bairro
    pessoa.cidade = cidade
    pessoa.estado = estado
    pessoa.telefone = telefone
    pessoa.celular = celular
    pessoa.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaCadastro(conexao)
    colecao.update(id=id, nome=nome, endereco=endereco, numero=numero, bairro=bairro, cidade=cidade, estado=estado, telefone=telefone, celular=celular)

    return redirect('doacao_info')

def PFdelete(request,id):                  
        user = get_object_or_404(User, id=id)
        user.delete()

        pessoas = PessoaCadastro.objects.get(id=id)
        pessoas.delete()

        conexao = ConexaoDATABASE()
        colecao = CRUD_PessoaCadastro(conexao)
        colecao.delete()

        return redirect('index')
# Fim PessoaCadastro

# Começo doacoes
def DCvisualizar(request): 
    if request.user.is_authenticated:
        id = request.session.get('id')
    if id is not None:
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

def DCupdate(request, id):
    item = request.POST.get("item")
    quantidade = request.POST.get("quantidade")
    medida = request.POST.get("medida")
    validade = request.POST.get("validade")

    doacao = ItemsDoacao.objects.get(id=id)
    doacao.item = item
    doacao.quantidade = quantidade
    doacao.medida = medida
    doacao.validade = validade
    doacao.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.update(id=id, item=item, quantidade=quantidade, medida=medida, validade=validade)

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
    pessoas = request.POST.get("pessoas")
    sobre = request.POST.get("sobre")
    encontrou = request.POST.get("encontrou")
    declaracao = request.POST.get("declaracao")
    
    user = PessoaApoio.objects.filter(cpf=cpf).first()
    if user:
            return HttpResponse('<h2> Já tem uma solicitação com este cpf </h2>') 
    data = datetime.datetime.today().strftime("%d-%m-%Y")
    
    PessoaApoio.objects.create(cpf = cpf,rg = rg,orgao = orgao,nome = nome,idade = idade,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,renda = renda,pessoas = pessoas,sobre = sobre,encontrou = encontrou,declaracao = declaracao)
    pessoa = PessoaApoio.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaApoio(conexao)
    colecao.insert(cpf = cpf,rg = rg,orgao = orgao,nome = nome,idade = idade,endereco = endereco,numero = numero,bairro = bairro,cidade = cidade,estado = estado,telefone = telefone,celular = celular ,renda = renda,pessoas = pessoas,sobre = sobre,encontrou = encontrou,declaracao = declaracao)
    
    file_title = cpf
    with open(f"{file_title}.txt", "w") as f:
        f.write(f"Data do pedido: {data}\nCPF: {cpf}\tRG: {rg}\nNome: {nome}\tIdade: {idade}\nEndereço: {endereco}\tnº {numero}\tBairro: {bairro}\nCidade: {cidade}\tEstado: {estado}\nTelefone: {telefone}\tCelular: {celular}\nRenda: {renda}\tNº Pessoas: {pessoas}\nSobre: {sobre}\nEncontrou: {encontrou}\tDeclaração: {declaracao}")

    return render(request, "index.html", {"pessoa": pessoa})

# Fim Apoio

# # Começo Login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username, password=password)
        
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
    pessoas = PessoaCadastro.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})
   
def usuario_index(request):
    if request.user.is_authenticated:
        id = request.session.get('id')
    if id is not None:
        usuario = User.objects.filter(id=id)
        return render(request, "doacao_index.html", {"usuario": usuario})
    else:
        return HttpResponse('<h1>ACESSO NEGADO!!! - Informações da sessão não encontradas</h1>')

def usuario_alterar(request,id):
    user = User.objects.get(id=id)
    return render(request,"usuario_editar.html", {"user": user})

def usuario_editar(request, id):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')

    user = User.objects.get(id=id)
    user.username = new_username
    user.email = new_email
    user.set_password(new_password)
    user.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaCadastro(conexao)
    colecao.update(id=id, username=new_username, email=new_email, password=new_password)

    return redirect("logout")


def botao(request):
    if request.user.is_authenticated:
        return render(request,"doacao_index.html")
    return render(request, 'junte.html')

def doacao_info(request):
    id = request.session.get('id')
    user = User.objects.filter(id=id)
    pessoas = PessoaCadastro.objects.filter(id=id)
    return render(request,"doacao_info.html", {"user": user,"pessoas": pessoas })
    

def doacao_suporte(request):
    return render(request, 'doacao_suporte.html')

def doacao_relatorio(request):
    if request.user.is_authenticated:
        id = request.session.get('id')
    if id is not None:
        item = request.POST.get("item")

        conexao = ConexaoDATABASE()
        consulta = Consultas(conexao)

        doacoes = ItemsDoacao.objects.all()
        total_doacoes = consulta.Total_doacoes()
        
        doacoes_por_item = consulta.doacoes_por_item(item)
        quantidade_total = consulta.quantidade_total_por_item(item)
        valor_medio = consulta.valor_medio_total()
        
        return render(request, 'doacao_relatorio.html', {"valor_medio":valor_medio,"doacoes": doacoes, 'total_doacoes': total_doacoes,'doacoes_por_item': doacoes_por_item, 'quantidade_total': quantidade_total})

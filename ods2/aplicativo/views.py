import datetime
from django.shortcuts import render, redirect
from aplicativo.models import ItemsDoacao, PessoaApoio, PessoaFisica, PessoaJuridica
from aplicativo.services.ConexaoMongoDB import CRUD_ItemsDoacao, CRUD_PessoaApoio, CRUD_PessoaFisica, CRUD_PessoaJuridica, ConexaoDATABASE, Find_Login

# Começo PessoaFisica
def PFvisualizar(request):
    pessoas = PessoaFisica.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})

def PFsalvar(request):
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

    PessoaFisica.objects.create(email=email,senha=senha,cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
                   numero=numero,bairro=bairro,cidade=cidade,estado=estado,telefone=telefone,celular=celular,
                   sobre=sobre,encontrou=encontrou,declaracao=declaracao)
    pessoas = PessoaFisica.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaFisica(conexao)
    colecao.insert(email=email,senha=senha,cpf=cpf,rg=rg,orgao=orgao,nome=nome,idade=idade,endereco=endereco,
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

    PessoaJuridica.objects.create(email=email,senha=senha,cnpj=cnpj,empresa=empresa,responsavel=responsavel,
                                  cargo=cargo,endereco=endereco,numero=numero,bairro=bairro,cidade=cidade,
                                  estado=estado,telefone=telefone,celular=celular,sobre=sobre,encontrou=encontrou,
                                  declaracao=declaracao)
    pessoas = PessoaJuridica.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_PessoaJuridica(conexao)
    colecao.insert(email=email,senha=senha,cnpj=cnpj,empresa=empresa,responsavel=responsavel,
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
    return render(request,"usuario_relatorios.html", {"doacoes": doacoes})

def DCsalvar(request):
    dia = request.POST.get("dia")
    item = request.POST.get("item")
    quantidade = request.POST.get("quantidade")
    peso = request.POST.get("peso")
    validade = request.POST.get("validade")

    ItemsDoacao.objects.create(dia=dia,item=item,quantidade=quantidade,peso=peso,validade=validade)
    doacoes = ItemsDoacao.objects.all()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.insert(item=item,quantidade=quantidade,peso=peso,validade=validade)
    return render(request,"usuario_relatorios.html", {"doacoes": doacoes})

def DCeditar(request,id):
    doacao = ItemsDoacao.objects.get(id=id)
    return render(request,"update.html", {"doacao": doacao})

def DCupdate(request,id):
    item = request.POST.get("item")
    quantidade = request.POST.get("quantidade")
    peso = request.POST.get("peso")
    validade = request.POST.get("validade")
    doacao = ItemsDoacao.objects.get(id=id)
    doacao.item=item,quantidade=quantidade,peso=peso,validade=validade
    doacao.save()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.update(item=item,quantidade=quantidade,peso=peso,validade=validade)

    return redirect('usuario_index')

def DCdelete(request,id):
    pessoas = ItemsDoacao.objects.get(id=id)
    pessoas.delete()

    conexao = ConexaoDATABASE()
    colecao = CRUD_ItemsDoacao(conexao)
    colecao.delete()

    return redirect('usuario_index')    
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

# Começo Login 
def Login(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        conexao = ConexaoDATABASE()
        colecao = Find_Login(conexao) 

        clientePF = colecao.find_one({'email': email, 'senha': senha})
        clientePJ = colecao.find_one2({'email': email, 'senha': senha})

        if clientePF or clientePJ:
            return redirect('usuario_index')
        else:
            return redirect('junte')
# Fim Login

# Começo Logout
def Logout(request):
   return render(request, 'index.html')
# Fim Logout

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
def usuario_index(request):
    pessoas = PessoaFisica.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})
def base2(request):
    pessoas = PessoaFisica.objects.all()
    return render(request,"usuario_index.html", {"pessoas": pessoas})

def usuario_cad_doacao(request):
    doacao = ItemsDoacao.objects.all()
    return render(request,"usuario_cad_doacao.html", {"doacao": doacao})
def usuario_relatorios(request):
    return render(request, 'usuario_relatorios.html')
def usuario_att_dados(request):
    return render(request, 'usuario_att_dados.html')
# Fim Renders
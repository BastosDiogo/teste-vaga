from django.shortcuts import render
from api.models import Produtos, Categoria, Fornecedor

def index(request):
    return render(request, "produtos\index.html")

def buscar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, r"produtos\buscar_fornecedores.html", {"fornecedores":fornecedores})

def buscar_produtos(request):
    produtos = Produtos.objects.all()
    return render(request, r"produtos\buscar_produtos.html", {"produtos":produtos})

def buscar_categorias(request):
    categorias = Categoria.objects.all()
    for categoria in categorias:
        categoria_tratada = str(categoria.nome_categoria).upper()
        categoria.nome_categoria = categoria_tratada
    return render(request, r"produtos\buscar_categorias.html",{"categorias":categorias})

def alterar_fornecedor(request):
    return render(request, r"produtos\alterar_fornecedor.html")

def alterar_produto(request):
    return render(request, r"produtos\alterar_produto.html")

def alterar_categoria(request):
    return render(request, r"produtos\alterar_categoria.html")

def criar_produto(request):
    mensagem = None
    lista_de_categorias = Categoria.objects.all()
    categorias = [str(categoria.nome_categoria).upper() for categoria in lista_de_categorias]
    lista_de_fornecedores = Fornecedor.objects.all()
    fornecedores_listados = [str(fornecedor.razao_social).upper() for fornecedor in lista_de_fornecedores]

    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        fornecedores = request.POST.get('fornecedores')
        Categoria(nome_categoria='nome_categoria')
        novo_produto = Produtos(
            nome=str(nome).upper(),
            categoria=str(categoria).upper(),
            fornecedores=str(fornecedores).upper(),
            descricao=descricao
        )
        novo_produto.save()
        mensagem = {"mensagem": "Produto criado com sucesso!"}

    return render(
        request,
        "produtos\criar_produto.html",
        {'lista_de_categorias':categorias,
         "lista_de_fornecedores":fornecedores_listados},
        mensagem
    )

def criar_fornecedor(request):
    mensagem = None
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')
        fornecedor = request.POST.get('fornecedor')
        razao_social = request.POST.get('razao_social')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        novo_fornecedor = Fornecedor(
            nome_fantasia=str(fornecedor).upper(),
            razao_social=str(razao_social).upper(),
            cnpj=str(cnpj).replace('.','').replace('-','').replace('/',''),
            telefone=telefone,
            endereco=endereco
        )
        novo_fornecedor.save()
        mensagem = {"mensagem": "Fornecedor criado com sucesso!"}
    return render(request, "produtos\criar_fornecedor.html", mensagem)

def criar_categoria(request):
    mensagem = None
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        if categoria:
            nova_categoria = Categoria(nome_categoria=str(categoria).upper())
            nova_categoria.save()
            mensagem = {"mensagem": "Categoria criada com sucesso!"}

    return render(request, "produtos\criar_categoria.html", mensagem)


def deletar_fornecedor(request):
    mensagem = None
    if request.method == 'POST':
        cnpj = (request.POST.get('cnpj'))
        cnpj = str(cnpj).replace('.','').replace('-','').replace('/','')
        Fornecedor.objects.filter(cnpj=cnpj).delete()
        mensagem = {"mensagem": f"Fornecedor {cnpj} apagado com sucesso!"}
    return render(request, "produtos\deletar_fornecedor.html", mensagem)


def deletar_produto(request):
    mensagem = None
    if request.method == 'POST':
        nome_produto = (request.POST.get('nome_produto'))
        nome_produto = str(nome_produto).replace('.','').replace('-','').replace('/','')
        Produtos.objects.filter(nome=nome_produto).delete()
        mensagem = {"mensagem": f"Produto {nome_produto} apagado com sucesso!"}
    return render(request, "produtos\deletar_produto.html", mensagem)

def deletar_categoria(request):
    mensagem = None
    if request.method == 'POST':
        categoria = (request.POST.get('categoria'))
        categoria = str(categoria).replace('.','').replace('-','').replace('/','')
        Categoria.objects.filter(nome_categoria=categoria).delete()
        mensagem = {"mensagem": f"Categoria {categoria} apagada com sucesso!"}
    return render(request, "produtos\deletar_categoria.html", mensagem)

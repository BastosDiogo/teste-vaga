from django.shortcuts import render

def index(request):
    return render(request, "produtos\index.html")

def buscar_fornecedores(request):
    return render(request, r"produtos\buscar_fornecedores.html")

def buscar_produtos(request):
    return render(request, r"produtos\buscar_produtos.html")

def alterar_fornecedor(request):
    return render(request, r"produtos\alterar_fornecedor.html")

def alterar_produto(request):
    return render(request, r"produtos\alterar_produto.html")

def criar_produto(request):
    return render(request, "produtos\criar_produto.html")

def criar_fornecedor(request):
    return render(request, "produtos\criar_fornecedor.html")

def deletar_fornecedor(request):
    return render(request, "produtos\deletar_fornecedor.html")

def deletar_produto(request):
    return render(request, "produtos\deletar_produto.html")

# def imagem(request):
#     return render(request, "galeria\imagem.html")
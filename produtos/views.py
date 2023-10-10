from django.shortcuts import render

def index(request):
    return render(request, "produtos\index.html")

def alterar_fornecedor(request):
    return render(request, r"produtos\alterar_fornecedor.html")
# def imagem(request):
#     return render(request, "galeria\imagem.html")
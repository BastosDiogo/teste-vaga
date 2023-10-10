from django.urls import path
from produtos.views import index, alterar_fornecedor

urlpatterns = [
    path('', index, name='index'),
    path('alterar-fornecedor/', alterar_fornecedor, name='alterar_fornecedor')
    # path('imagem/', imagem, name='imagem')
]

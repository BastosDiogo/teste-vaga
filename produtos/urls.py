from django.urls import path
from produtos.views import (
    index,
    alterar_fornecedor,
    alterar_produto,
    alterar_categoria,
    buscar_fornecedores,
    buscar_produtos,
    buscar_categorias,
    criar_fornecedor,
    criar_produto,
    criar_categoria,
    deletar_fornecedor,
    deletar_produto,
    deletar_categoria,
)

urlpatterns = [
    path('', index, name='index'),
    path('alterar-fornecedor/', alterar_fornecedor, name='alterar_fornecedor'),
    path('alterar-produto/', alterar_produto, name='alterar_produto'),
    path('alterar-categoria/', alterar_categoria, name='alterar_categoria'),
    path('buscar-fornecedores/', buscar_fornecedores, name='buscar_fornecedores'),
    path('buscar-produtos/', buscar_produtos, name='buscar_produtos'),
    path('buscar-categorias/', buscar_categorias, name='buscar_categorias'),
    path('criar-produto/', criar_produto, name='criar_produto'),
    path('criar-fornecedor/', criar_fornecedor, name='criar_fornecedor'),
    path('criar-categoria/', criar_categoria, name='criar_categoria'),
    path('deletar-produto/', deletar_produto, name='deletar_produto'),
    path('deletar-fornecedor/', deletar_fornecedor, name='deletar_fornecedor'),
    path('deletar-categoria/', deletar_categoria, name='deletar_categoria'),
]

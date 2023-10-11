from rest_framework import viewsets
from api.models import Produtos, Categoria, Fornecedor
from api.serializer import (
    ProdutoSerializers,
    CategoriaSerializers,
    FornecedorSerializers
)

class ProdutosViewSets(viewsets.ModelViewSet):
    """Exisbir todos os produtos cadastrados"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializers


class CategoriaViewSets(viewsets.ModelViewSet):
    """Exisbir todos as categorias cadastradas"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers


class FornecedorViewSets(viewsets.ModelViewSet):
    """Exisbir todos os fonecedores cadastrados"""
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializers
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Produtos, Categoria, Fornecedor
from api.serializer import (
    ProdutoSerializers,
    CategoriaSerializers,
    FornecedorSerializers,
    ListaFornecedoreSerializers
)

class ProdutosViewSets(viewsets.ModelViewSet):
    """Exisbir todos os produtos cadastrados"""
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializers
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['nome']
    search_fields = ['nome']


class CategoriaViewSets(viewsets.ModelViewSet):
    """Exisbir todos as categorias cadastradas"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome_categoria']


class FornecedorViewSets(viewsets.ModelViewSet):
    """Exisbir todos os fonecedores cadastrados"""
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializers
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    ordering_fields = ['razao_social']
    search_fields = ['razao_social','cnpj']


class ListaFornecedor(generics.ListAPIView):
    """Listando os fornecedores"""
    def get_queryset(self):
        queryset = Fornecedor.objects.filter(cnpj=self.kwargs['pk'])
        return queryset
    serializer_class = ListaFornecedoreSerializers
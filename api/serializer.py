from rest_framework import serializers
from api.models import Produtos, Categoria, Fornecedor

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = [
            'nome',
            'categoria',
            'data_cadastro',
            'data_atualizacao',
            'fornecedores',
            'descricao'
        ]


class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class FornecedorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ListaFornecedoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'
from django.contrib import admin
from api.models import Produtos, Categoria, Fornecedor

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("nome", "categoria","data_cadastro","data_atualizacao","fornecedores")
    list_display_links = ("nome",)
    search_fields = ("nome","categoria")
    list_per_page = 20
    ordering = ('nome',)

class ListandoCategorias(admin.ModelAdmin):
    list_display = ("nome_categoria",)
    list_display_links = ("nome_categoria",)
    search_fields = ("nome_categoria",)
    list_per_page = 20
    ordering = ('nome_categoria',)

class ListandoFornecedores(admin.ModelAdmin):
    list_display = ("cnpj","razao_social","nome_fantasia","telefone")
    list_display_links = ("razao_social","cnpj")
    search_fields = ("razao_social","cnpj")
    list_per_page = 20
    ordering = ('razao_social',)

admin.site.register(Produtos, ListandoProdutos)
admin.site.register(Categoria, ListandoCategorias)
admin.site.register(Fornecedor, ListandoFornecedores)
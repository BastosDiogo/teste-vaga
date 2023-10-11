from django.contrib import admin
from django.urls import path, include
from api.views import (
    ProdutosViewSets,
    CategoriaViewSets,
    FornecedorViewSets,
    ListaFornecedor
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produto', ProdutosViewSets, 'api_produto')
router.register('categoria', CategoriaViewSets, 'api_categoria')
router.register('fornecedor', FornecedorViewSets, 'api_fornecedor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("produtos.urls")),
    path('api/', include(router.urls)),
    path('api/buscar-fornecedor/<int:pk>/', ListaFornecedor.as_view()),
]
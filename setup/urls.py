from django.contrib import admin
from django.urls import path, include
from api.views import (
    ProdutosViewSets,
    CategoriaViewSets,
    FornecedorViewSets
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api-produto', ProdutosViewSets, 'api_produto')
router.register('api-categoria', CategoriaViewSets, 'api_categoria')
router.register('api-fornecedor', FornecedorViewSets, 'api_fornecedor')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("produtos.urls")),
    path('api/', include(router.urls)),
]
from django.db import models

class Categoria(models.Model):

    nome_categoria = models.CharField(max_length=100, null=False, blank=False,primary_key=True)

    def __str__(self):
        return f"{self.nome_categoria}".upper()

    def __rep__(self):
        return str(self.nome_categoria).lower()


class Fornecedor(models.Model):

    nome_fantasia = models.CharField(max_length=100, null=False, blank=False)
    razao_social = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False, primary_key=True)
    telefone = models.CharField(max_length=12, null=False, blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.razao_social}".upper()


class Produtos(models.Model):

    nome = models.CharField(max_length=200, null=False, blank=False, primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(blank=False, auto_now=True, null=False)
    data_atualizacao = models.DateTimeField(blank=False, auto_now=True, null=False)
    fornecedores = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
    descricao = models.CharField(max_length=600, blank=True, null=True)

    def __str__(self):
        return f"{self.nome}".capitalize()

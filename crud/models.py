from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
SIGLAS = (('ac', 'AC'),('al', 'AL'),('ap', 'AP'),('am', 'AM'),('ba', 'BA'),('ce', 'CE'),('df', 'DF'),
('es', 'ES'),('go', 'GO'),('ma', 'MA'),('mt', 'MT'),('ms', 'MS'),('mg', 'MG'),('pa', 'PA'),('pb', 'PB'),
('pr', 'PR'),('pe', 'PE'),('pi', 'PI'),('rj', 'RJ'),('rn', 'RN'),('rs', 'RS'),('ro', 'RO'),('rr', 'RR'),
('sc', 'SC'),('sp', 'SP'),('se', 'SE'),('to', 'TO'))

class Base(models.Model):
    criacao = models.DateField('Criado', auto_now_add=True)
    alteracao = models.DateTimeField('Alterado', auto_now=True)
    class Meta:
        abstract = True

class Fornecedores(Base):
    nome = models.CharField('Nome fornecedor', max_length=50)
    cep = models.IntegerField('CEP', default=0)

    def __str__(self):
        return f'{self.nome}'

class CadastroProdutos(Base):
    nome = models.CharField('Nome', max_length=20)
    estoque = models.IntegerField('Estoque')
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, default=0)
    valor_de_venda = models.DecimalField('Preço de Venda', max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.nome}'
   

class VendaProduto(Base):
    produto = models.ForeignKey(CadastroProdutos, on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField('Quantidade', default=0)

from django import forms
from django.db.models import fields
from .models import CadastroProdutos, Fornecedores, VendaProduto

class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = CadastroProdutos
        fields = ['nome', 'estoque', 'fornecedor', 'valor_de_venda']

class CadastroFornecedoresForm(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = ['nome', 'cep']

class RegistroVendaForm(forms.ModelForm):
    class Meta:
        model = VendaProduto
        fields = ['produto', 'quantidade']
        

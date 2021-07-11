from django.core import paginator
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .forms import CadastroModelForm, CadastroFornecedoresForm, RegistroVendaForm
from .models import CadastroProdutos, Fornecedores, VendaProduto
from django.contrib import messages


# Create your views here.

def cliList(request):
    clientes = CadastroProdutos.objects.all().order_by('-criacao')

    context = {
        'tasks': clientes
    }    
    return render(request, 'tasks/list.html', context)

def cadastroClientes(request):
    if str(request.method) == 'POST':
        form = CadastroModelForm(request.POST or None)
        if form.is_valid():
            form.save()

            form = CadastroModelForm()
            messages.success(request, 'Formulário enviado com sucesso')
        else:
            messages.error(request, 'Erro ao enviar formulário')
    else:
        form = CadastroModelForm()

    context = {
        'form': form
    }
    return render(request, 'tasks/cadastro.html', context)

def conteudo(request, id):
    cliente = get_object_or_404(CadastroProdutos, pk=id)
    # status = 'Ativo' if cliente.ativo else 'Inativo'
    context = {
        'cliente': cliente,
        # 'status': status
    }
    return render(request, 'tasks/conteudo.html', context)

def update(request, id):
    cliente = CadastroProdutos.objects.get(id=id)
    form = CadastroModelForm(instance=cliente)
    

    context = {
        'cliente': cliente,
        'form': form,
    }
    if str(request.method)=='POST':
        form = CadastroModelForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'tasks/update.html', context)
    else:
        return render(request, 'tasks/update.html', context)

def delete(request, id):
    cliente = get_object_or_404(CadastroProdutos, pk=id)
    cliente.delete()
    
    return redirect('/')

def fornecedoresList(request):
    fornecedores = Fornecedores.objects.all()
    context = {
        'fornecedores': fornecedores,
    }
    return render(request, 'tasks/forneList.html', context)
def conteudoForn(request, id):
    fornecedor = get_object_or_404(Fornecedores, pk=id)
    context = {
        'fornecedor': fornecedor,
    }
    return render(request, 'tasks/conteudoForne.html', context)
def cadastroForn(request):
    if str(request.method) == 'POST':
        form = CadastroFornecedoresForm(request.POST or None)
        if form.is_valid():
            form.save()

            form = CadastroFornecedoresForm()
            messages.success(request, 'Formulário enviado com sucesso')
        else:
            messages.error(request, 'Erro ao enviar formulário')
    else:
        form = CadastroFornecedoresForm()

    context = {
        'form': form
    }
    return render(request, 'tasks/cadForne.html', context)

def updateForn(request, id):
    cliente = Fornecedores.objects.get(id=id)
    form = CadastroFornecedoresForm(instance=cliente)

    context = {
        'cliente': cliente,
        'form': form,
    }
    if str(request.method)=='POST':
        form = CadastroFornecedoresForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/flist')
        else:
            return render(request, 'tasks/updateForne.html', context)
    else:
        return render(request, 'tasks/updateForne.html', context)

def deleteForn(request, id):
    cliente = get_object_or_404(Fornecedores, pk=id)
    cliente.delete()
    
    return redirect('/flist')

def venda_registro(request):
    if str(request.method) == 'POST':
        form = RegistroVendaForm(request.POST or None)
        produto = CadastroProdutos.objects.get(pk = int(form.data['produto']))
        produto.estoque -= int(form.data['quantidade'])
        produto.save()
        
        if form.is_valid():
            form.save()
    else:
        form = RegistroVendaForm()
    
    context = {
        'form': form
    }
    template_name = 'tasks/vendaRegistro.html'
    return render(request, template_name, context)
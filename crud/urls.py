from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliList, name='cliente-list'),
    path('cadastro', views.cadastroClientes, name='cadastro'),
    path('update/<int:id>', views.update, name='update'),
    path('conteudo/<int:id>', views.conteudo, name='conteudo'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('flist/', views.fornecedoresList, name='listForne'),
    path('cadastro-forne/', views.cadastroForn, name='cadastro-forne'),
    path('flist/updateForne/<int:id>', views.updateForn, name='updateForne'),
    path('conteudoForne/<int:id>', views.conteudoForn, name='conteudoForne'),
    path('flist/deleteForne/<int:id>', views.deleteForn, name='deleteForne'),
    path('venda-registro/', views.venda_registro, name='venda_registro'),
]
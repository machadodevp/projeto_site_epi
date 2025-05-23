from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Rota para o formulário de cadastro

    # coloaborador
    path('cadastro_colaborador/', views.cadastro_colaborador, name='cadastro_colaborador'),  # Rota para o formulário de cadastro
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),  # Página de sucesso
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),  # Lista de colaboradores
     path('colaborador/editar/<int:colaborador_id>/', views.editar_colaborador, name='editar_colaborador'),
    path('colaborador/deletar/<int:colaborador_id>/', views.deletar_colaborador, name='deletar_colaborador'),
    
    
    # URLS DE EQUIPAMENTOS
    path('cadastro_equipamento/', views.cadastro_equipamento, name='cadastro_equipamento'),
    path('equipamentos/', views.lista_equipamentos, name='lista_equipamentos'),
     # URL para editar um equipamento
    path('editar/equipamento/<int:equipamento_id>/', views.editar_equipamento, name='editar_equipamento'),
    
    # URL para deletar um equipamento
    path('deletar/equipamento/<int:equipamento_id>/', views.deletar_equipamento, name='deletar_equipamento'),

    # URL tela de controle
    path('registrar_acao/', views.registrar_acao, name='registrar_acao'),
    path('acoes/', views.lista_acao, name='lista_acao'),

]

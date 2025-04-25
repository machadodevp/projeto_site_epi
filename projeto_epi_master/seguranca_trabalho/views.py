from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaborador, Equipamento


# Página inicial
def home(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'cadastro/home.html', {'equipamentos': equipamentos})


# ----------------- COLABORADOR -------------------

def cadastro_colaborador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cargo = request.POST.get('cargo')

        # Validação simples
        if not nome or not idade or not email or not telefone or not cargo:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return redirect('cadastro_colaborador')

        colaborador = Colaborador(
            nome=nome,
            idade=idade,
            email=email,
            telefone=telefone,
            cargo=cargo
        )
        colaborador.save()
        return redirect('cadastro_sucesso')

    return render(request, 'cadastro/colaborador_form.html')


def cadastro_sucesso(request):
    return render(request, 'cadastro/sucesso.html')


def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all().order_by('nome')
    return render(request, 'cadastro/lista_colaboradores.html', {'colaboradores': colaboradores})


# ----------------- EQUIPAMENTO -------------------

def cadastro_equipamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        numero_serie = request.POST.get('numero_serie')
        fabricante = request.POST.get('fabricante')  # ← NOVO CAMPO

        if not nome or not tipo or not numero_serie or not fabricante:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return redirect('cadastro_equipamento')

        equipamento = Equipamento(
            nome=nome,
            tipo=tipo,
            numero_serie=numero_serie,
            fabricante=fabricante  # ← Salvando o novo campo
        )
        equipamento.save()

        messages.success(request, 'Equipamento cadastrado com sucesso!')
        return redirect('lista_equipamentos')

    return render(request, 'cadastro/cadastro_equipamento.html')


def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all().order_by('nome')
    return render(request, 'cadastro/lista_equipamentos.html', {'equipamentos': equipamentos})



def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        numero_serie = request.POST.get('numero_serie')
        fabricante = request.POST.get('fabricante')

        if not nome or not tipo or not numero_serie or not fabricante:
            messages.error(request, 'Todos os campos são obrigatórios!')
            return redirect('editar_equipamento', equipamento_id=equipamento.id)

        equipamento.nome = nome
        equipamento.tipo = tipo
        equipamento.numero_serie = numero_serie
        equipamento.fabricante = fabricante
        equipamento.save()

        messages.success(request, 'Equipamento atualizado com sucesso!')
        return redirect('lista_equipamentos')

    return render(request, 'cadastro/editar_equipamento.html', {'equipamento': equipamento})


def deletar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_id)
    equipamento.delete()
    messages.success(request, 'Equipamento deletado com sucesso!')
    return redirect('lista_equipamentos')

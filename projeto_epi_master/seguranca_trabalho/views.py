from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaborador, Equipamento, Acao


# Página inicial
def home(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'home.html', {'equipamentos': equipamentos})


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

# Editar
def editar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if request.method == 'POST':
        colaborador.nome = request.POST.get('nome')
        colaborador.idade = request.POST.get('idade')
        colaborador.email = request.POST.get('email')
        colaborador.telefone = request.POST.get('telefone')
        colaborador.cargo = request.POST.get('cargo')
        colaborador.save()
        messages.success(request, 'Colaborador atualizado com sucesso!')
        return redirect('lista_colaboradores')

    return render(request, 'cadastro/colaborador_form.html', {'colaborador': colaborador})


# Deletar
def deletar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)
    
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador deletado com sucesso!')
        return redirect('lista_colaboradores')
    
    return render(request, 'cadastro/confirmar_delete.html', {'colaborador': colaborador})
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

#--------------Tela de controle-----------------------



def registrar_acao(request):
    colaboradores = Colaborador.objects.all()
    equipamentos = Equipamento.objects.all()

    if request.method == 'POST':
        equipamento_id = request.POST.get('equipamento')
        colaborador_id = request.POST.get('colaborador')
        data_emprestimo = request.POST.get('data_emprestimo')
        data_prevista = request.POST.get('data_prevista_devolucao')
        status = request.POST.get('status')
        condicoes = request.POST.get('condicoes_emprestimo')
        data_devolucao = request.POST.get('data_devolucao') or None
        observacao = request.POST.get('observacao') or None

        if not equipamento_id or not colaborador_id or not data_emprestimo or not data_prevista or not status or not condicoes:
            messages.error(request, "Preencha todos os campos obrigatórios.")
            return redirect('registrar_acao')

        acao = Acao.objects.create(
            equipamento_id=equipamento_id,
            colaborador_id=colaborador_id,
            data_emprestimo=data_emprestimo,
            data_prevista_devolucao=data_prevista,
            status=status,
            condicoes_emprestimo=condicoes,
            data_devolucao=data_devolucao,
            observacao=observacao
        )
        messages.success(request, "Ação registrada com sucesso!")
        return redirect('registrar_acao')

    return render(request, 'cadastro/registrar_acao.html', {'colaboradores': colaboradores, 'equipamentos': equipamentos})

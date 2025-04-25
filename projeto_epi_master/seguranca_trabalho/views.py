from django.shortcuts import render
from .models import Colaborador, Equipamento


# Create your views here.



from django.shortcuts import render, redirect
from .models import Colaborador
# Função para exibir a página inicial
def home(request):
    return render(request, 'cadastro/home.html')
                  
def cadastro_colaborador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cargo = request.POST.get('cargo')

        # Salva os dados no banco
        colaborador = Colaborador(
            nome=nome,
            idade=idade,
            email=email,
            telefone=telefone,
            cargo=cargo
        )
        colaborador.save()

        return redirect('cadastro_sucesso')  # Redireciona para uma página de sucesso

    return render(request, 'cadastro/colaborador_form.html')

def cadastro_sucesso(request):
    return render(request, 'cadastro/sucesso.html')

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()  # Busca todos os colaboradores
    return render(request, 'cadastro/lista_colaboradores.html', {'colaboradores': colaboradores})

# -----------------EQUIPAMENTOS-------------------

def cadastro_equipamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        numero_serie = request.POST.get('numero_serie')

        equipamento = Equipamento(
            nome=nome,
            tipo=tipo,
            numero_serie=numero_serie
        )
        equipamento.save()

        return redirect('lista_equipamentos')  # Redireciona para a lista

    return render(request, 'cadastro/cadastro_equipamento.html')


def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'cadastro/lista_equipamentos.html', {'equipamentos': equipamentos})



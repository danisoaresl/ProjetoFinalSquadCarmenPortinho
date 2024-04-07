from django.shortcuts import render, redirect
from django.contrib import messages
from adocao.forms import SolicitacaoAdocaoForm
from animal.models import Animal

def solicitar_adocao(request):
    animais_disponiveis = Animal.objects.filter(adotado=False)
    if request.method == 'POST':
        form = SolicitacaoAdocaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitação de adoção enviada com sucesso!')
            return redirect('animais:listar_animais')
    else:
        form = SolicitacaoAdocaoForm()

    contexto = {
        'form': form,
        'animais_disponiveis': animais_disponiveis,
    }
    return render(request, 'solicitar_adocao.html', contexto)
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm, NameForm

# Create your views here.


# Adicionando sistema de autenticação
# @login_required
# app_label.op - verifique no banco de dados as permissões disponíveis
@permission_required(
    'contacts.add_contact'
)  # Requer autenticação antes de verificar permissão
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect(f'{settings.LOGIN_URL}?next={request.path}')
    # Substituído pelo decorador

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['sender'].split('@')[0]
            return HttpResponseRedirect(reverse('contacts:thanks', args=(name,)))
    else:
        form = ContactForm()

    return render(request, 'contacts/create.html', {'form': form})


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        # A validação do formulário fica a cargo do Django
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return HttpResponseRedirect(reverse('contacts:thanks', args=(name,)))

    else:
        form = NameForm()

    return render(request, 'contacts/name.html', {'form': form})


def thanks(request, name):
    # request.GET['name']
    return HttpResponse(f'Obrigado {name}')

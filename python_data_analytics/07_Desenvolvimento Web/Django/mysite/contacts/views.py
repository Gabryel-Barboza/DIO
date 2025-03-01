from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm, NameForm

# Create your views here.


def create(request):
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

from django.shortcuts import render, redirect
from .models import Instruments, Calipers, Micrometers
from .forms import CalipersForm, MicrometersForm
from django.views.generic import UpdateView, DeleteView


# Create your views here.

def instruments_home(request):
    instruments = Instruments.objects.order_by('title')
    return render(request, 'instruments/instruments_home.html', {'instruments': instruments})


class CalipersUpdateView(UpdateView):
    model = Calipers
    template_name = 'instruments/create.html'

    form_class = CalipersForm

class CalipersDeleteView(DeleteView):
    model = Calipers
    success_url = '/instruments/calipers'
    template_name = 'instruments/instruments_delete.html'


class MicrometersDeleteView(DeleteView):
    model = Micrometers
    success_url = '/instruments/micrometers'
    template_name = 'instruments/instruments_delete.html'

class MicrometersUpdateView(UpdateView):
    model = Micrometers
    template_name = 'instruments/create.html'

    form_class = MicrometersForm


def calipers(request):
    calipers = Calipers.objects.order_by('inv_number')
    return render(request, 'instruments/table_layout.html', {'title': 'Штангенциркули', 'instruments': calipers})


def micrometers(request):
    micrometers = Micrometers.objects.order_by('inv_number')
    return render(request, 'instruments/table_layout.html', {'title': 'Микрометры', 'instruments': micrometers})


def create_calipers(request):
    error = ''
    if request.method == 'POST':
        form = CalipersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calipers')
        else:
            error = 'Форма была неверной'
    form = CalipersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'instruments/create.html', data)


def create_micrometers(request):
    error = ''
    if request.method == 'POST':
        form = MicrometersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('micrometers')
        else:
            error = 'Форма была неверной'
    form = MicrometersForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'instruments/create.html', data)

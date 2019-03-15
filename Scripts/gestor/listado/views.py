from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import Http404
from .models import restaurante, Reserva
from .forms import NuevaReserva
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def lista(request):
    context = {
        'restaurantes': restaurante.objects.all()
    }
    return render_to_response('listado/listing.html', context)

# @login_required(login_url="/")
def detalles(request, pk):
    # context = {
    #     'restaurante': restaurante.objects.get(pk=pk)
    #     }
    # reserva = Reserva()
    form = NuevaReserva()
    context = {
        # 'User': User.objects.get(pk=pk),
        'restaurante': restaurante.objects.get(pk=pk),
        'form': form
    }
    if request.method == "POST":
        form = NuevaReserva(request.POST)
        form.restaurante = restaurante.pk
        if form.is_valid():
            form.restaurante = restaurante.pk
            form.save(commit=False)
            # form.usuario = User.pk
            form.save()

    return render(request,'listado/detail.html', context)

# def reservas(request):
#     form = NuevaReserva(request.POST)
#     if form.is_valid():
#             form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'listado/detail.html', context)

def gracias(request):
    return render(request,'listado/gracias.html') 

def menu(request):
    return render(request,'listado/menu.html') 

def final(request):
    return render(request,'listado/final.html') 

def final1(request):
    return render(request,'listado/final1.html') 

def pago(request):
    return render(request,'listado/pago.html') 
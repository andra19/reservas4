from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import Http404
from .models import restaurante
from .forms import NuevaReserva

def lista(request):
    context = {
        'restaurantes': restaurante.objects.all()
    }
    return render_to_response('listado/listing.html', context)


def detalles(request, pk):
    # context = {
    #     'restaurante': restaurante.objects.get(pk=pk)
    #     }
    if request.method == 'POST' :
        form = NuevaReserva(request.POST)
    if form.is_valid():
            form.save()
    context = {
        'restaurante': restaurante.objects.get(pk=pk),
        'form': form
    }
    return render('listado/detail.html', context)

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
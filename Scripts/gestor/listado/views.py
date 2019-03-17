from django.shortcuts import render_to_response, render, get_object_or_404
from .models import restaurante, Reserva
from .forms import NuevaReserva
from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class RestauranteListView(ListView):
    model = restaurante
    template_name = 'listado/listing.html'
    context_object_name = 'restaurantes'

class RestauranteDetailView(DetailView, CreateView):
    model = Reserva
    template_name = 'listado/detail.html'
    context_object_name = 'restaurantes'
    fields=['email', 'telefono', 'personas', 'dia', 'hora', 'restaurante']
    success_url= '/listado/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_queryset(self):
        return restaurante.objects.all()




# class ReservaCreateView(FormView):
#     template_name = 'listado/detail.html'
#     form_class = NuevaReserva
#     success_url = '/listado/'
#     fields = ['nombre', 'apellido', 'email', 'telefono', 'personas', 'dia', 'hora', 'restaurante', 'usuario' ]

#     def form_valid(self, form):
#         form.save()
#         return super(ReservaCreateView, self).form_valid(form)
#     context_object_name = 'reservas'
    




# def lista(request):
#     context = {
#         'restaurantes': restaurante.objects.all()
#     }
#     return render_to_response('listado/listing.html', context)

# @login_required(login_url="/")
# def detalles(request, pk):
    # context = {
    #     'restaurante': restaurante.objects.get(pk=pk)
    #     }
    # reserva = Reserva()
    # form = NuevaReserva()
    # context = {
        # 'User': User.objects.get(pk=pk),
        # 'restaurante': restaurante.objects.get(pk=pk),
        # 'form': form
    # }
    # if request.method == "POST":
    #     form = NuevaReserva(request.POST)
    #     form.restaurante = restaurante.pk
    #     if form.is_valid():
    #         form.restaurante = restaurante.pk
    #         form.save(commit=False)
    #         form.usuario = User.pk
    #         form.save()

    # return render(request,'listado/detail.html', context)

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
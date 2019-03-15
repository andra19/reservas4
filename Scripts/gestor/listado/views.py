from django.shortcuts import render_to_response, render, get_object_or_404
from .models import restaurante
from .forms import NuevaReserva
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required

class RestauranteListView(ListView):
    model = restaurante
    template_name = 'listado/listing.html'
    context_object_name = 'restaurantes'

class RestauranteDetailView(DetailView, FormView):
    model = restaurante
    form_class = NuevaReserva
    template_name = 'listado/detail.html'
    success_url = '/final/'
    context_object_name = 'restaurantes'

    def form_valid(self, form):
        form.save()
        return super(RestauranteDetailView, self).form_valid(form)




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
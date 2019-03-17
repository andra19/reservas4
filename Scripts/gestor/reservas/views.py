from django.shortcuts import render, render_to_response
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from listado.models import Reserva
# from django.urls import reverse_lazy 

class ReservaListView(ListView):
    # queryset = Reserva.objects.all()
    template_name = 'reservas/opciones.html'
    context_object_name = 'reservas'
    paginate_by = 5
    ordering = ['-id']

    def get_queryset(self):
        return Reserva.objects.filter(usuario=self.request.user)

     
    
class ReservaDetailView(DetailView, UpdateView, DeleteView):
    model = Reserva
    template_name = 'reservas/detalles.html'
    context_object_name = 'reservas'
    fields=['personas', 'dia', 'hora']
    success_url= '/reservas/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.save()
        return super().form_valid(form)

# class ReservaDeleteView(DeleteView):
#       model = Reserva
#       template_name = 'reservas/detalles.html'
#       context_object_name = 'reservas'
      
     




from django.shortcuts import render, render_to_response
# from .forms import NuevaReserva
def reservas(request):
      return render(request, 'reservas/opciones.html') 
# def reservas(request):
#     return render (request, 'reservas/cancelar.html')

# def reservas(request):
#     form = NuevaReserva(request.POST)
#     if form.is_valid():
#             form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'listado/detail.html', context)

# def reservas (request):
#     context = {
#         'nueva': NuevaReserva()
#     }
#     return render_to_response('listado/detail.html', context)

#     if request.method == 'POST':
#         form = NuevaReserva(request.POST)
#     else:
#         form = NuevaReserva()
#     return render (request, 'listado/detail.html', {'form':form})
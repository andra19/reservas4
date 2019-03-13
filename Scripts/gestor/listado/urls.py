from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='listado'),
    path('detalles/<int:pk>/', views.detalles, name='detalles'),
    # path('detalles/', views.reservas, name='NuevaReserva'),
    path('gracias/', views.gracias, name='gracias'),
    path('menu/', views.menu, name='menu'),
    path('final/', views.final, name='final'),
    path('final1/', views.final1, name='final1'),
    path('pago/', views.pago, name='pago')
]

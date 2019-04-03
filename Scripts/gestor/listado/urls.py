from django.urls import path
from .views import RestauranteListView, RestauranteDetailView, reservasView, MenuView
from . import views

urlpatterns = [
    # path('', views.lista, name='listado'),
    path('', RestauranteListView.as_view(), name='listado'),
    path('resturantes/<int:pk>/', RestauranteDetailView.as_view(), name='detalles'),
    # path('resturantes/<int:pk>/',views.detalles, name='detalles'),
    # path('detalles/', views.reservas, name='NuevaReserva'),
    path('gracias/', views.gracias, name='gracias'),
    path('menu/', MenuView.as_view(), name='menu'),
    path( 'final/', reservasView.as_view(), name='final'),
    path('final1/', views.final1, name='final1'),
    path('pago/', views.pago, name='pago')
]

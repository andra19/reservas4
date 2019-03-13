from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    return render(request, 'home/index.html') 

def info(request):
    return render(request,'home/informacion.html') 

def Login(request):
    if request.method == 'POST':
        AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect('listado/')
    else:
        form = AuthenticationForm()
    return render(request,'usuario/registro.html', {'form':form})








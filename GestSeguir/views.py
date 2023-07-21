from email import message
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
# Create your views here.

def home(request):
    
    return render(request, "ProyectoSegApp/home.html")

def servicios (request):
    
    return render(request, "ProyectoSegApp/servicios.html")

def cuestionario (request):

    return render(request, "ProyectoSegApp/cuestionario.html")

def blog(request):

    return render(request, "ProyectoSegApp/blog.html")

def contacto(request):
    return render(request, "ProyectoSegApp/contacto.html")

def enc_egre(request):

    return render(request, "ProyectoSegApp/enc_egre.html")

def enc_emp(request):
    return render(request, "ProyectoSegApp/enc_emp.html")

#def registro(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            message.success(request, 'Usuario {username} creado')
            return redirect('Home')
    else:
        form = UserCreationForm()
        
    context = { 'form' : form}
       
    return render(request,'ProyectoSegApp/registro.html', context)
    
    
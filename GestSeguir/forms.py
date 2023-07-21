from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

#class UserRegisterForm(UserCreationForm):
    
#    apepat = forms.CharField() 
#    apemat = forms.CharField() 
#    matric = forms.CharField()
#    direccion = forms.CharField() 
#    email = forms.EmailField() 
#    numero = forms.CharField()
#    carrera = forms.CharField()
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password1', 'password2']
#        help_texts = {k: "" for k in fields}

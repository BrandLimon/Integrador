from django.urls import path
from GestSeguir import views



urlpatterns = [
    path('',views. home, name="Home"),
    path('servicios/', views.servicios, name="servicios"),
    path('cuestionario/', views.cuestionario, name="cuestionario"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),
    path('enc_egre/', views.enc_egre, name="enc_egre"),
    path('enc_emp/', views.enc_emp, name="enc_emp")
    
    #path('registro/', views.registro, name='registro'),

]
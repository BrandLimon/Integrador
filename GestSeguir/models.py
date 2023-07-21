from django.db import models

# Create your models here.

class Egresado (models.Model):
    
    CARRERAS = (
        ('Ing. Agroindustrial','Ing. Agroindustrial'),
        ('Ing. de Software','Ing. de Software'),
        ('Ing. Animación y Efectos visuales','Ing. Animación y Efectos visuales'), 
        ('Ing. en Energia','Ing. en Energia'), 
        ('Ing. en Logistica y transporte','Ing. en Logistica y transporte'), 
        ('Ing. en Nanotecnologia','Ing. en Nanotecnologia'), 
        ('Ing. Sistemas automotices','Ing. Sistemas automotices'), 
        ('Ing. Tecnologia ambiental','Ing. Tecnologia ambiental'), 
        ('Ing. Financiera','Ing. Financiera'), 
        ('Ing. Mecatronica','Ing. Mecatronica')
      
    )
    
    nombre = models.CharField(max_length = 15) 
    apepat = models.CharField(max_length = 15) 
    apemat = models.CharField(max_length = 15) 
    matric = models.CharField(max_length = 6)
    direccion = models.CharField(max_length = 50) 
    email = models.EmailField(blank = True, null = True) 
    numero = models.CharField(max_length = 10)
    carrera = models.CharField(max_length=50,
                                choices=CARRERAS,
                                default='Ing. Agroindustrial')
    
    def _str_(self): 
        return 'El nombre es del egresado es: %s apellidos %s y %s, Matricula: %s, Direccion: %s, Email: %s, Telefono: %s' % (self.nombre, self.apepat, self.apemat, 
                                                                                                             self.matric, self.direccion,
                                                                                                             self.email, self.numero)
    
class Empleadore (models.Model):
    nombre = models.CharField(max_length = 15) 
    apepat = models.CharField(max_length = 15) 
    apemat = models.CharField(max_length = 15) 
    matric = models.CharField(max_length = 10)
    numcedula = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 50) 
    email = models.EmailField(blank = True, null = True) 
    numero = models.CharField(max_length=7)
    
    def _str_(self): 
        return 'El nombre del empleador es: %s apellidos %s y %s, Matricula: %s, Numero de cedula: %s Direccion: %s, Email: %s, Telefono: %s' % (self.nombre, self.apepat, 
                                                                                                             self.apemat, self.matric,
                                                                                                             self.numcedula, self.direccion,
                                                                                                             self.email, self.numero)
        
class Enc_egre (models.Model):
    pr1 = models.TextField(max_length = 999) 
    pr2 = models.TextField(max_length = 999) 
    pr3 = models.TextField(max_length = 999) 
    pr4 = models.TextField(max_length = 999)
    pr5 = models.TextField(max_length = 999)
    pr6 = models.TextField(max_length = 999) 
    

        
class Enc_emp (models.Model):
    pr1 = models.TextField(max_length = 999) 
    pr2 = models.TextField(max_length = 999) 
    pr3 = models.TextField(max_length = 999) 
    pr4 = models.TextField(max_length = 999)
    pr5 = models.TextField(max_length = 999)
    pr6 = models.TextField(max_length = 1000) 
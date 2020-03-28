from django.db import models

class Paseador(models.Model):
    idpas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    rating=models.IntegerField()
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    foto =models.ImageField(upload_to="paseadores",blank=True)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(unique=True, max_length=200, blank=True, null=True)
    foto =models.ImageField(upload_to="clientes",blank=True)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    SEXO =(('macho','macho'),('hembra','hembra'))
    TMASCOTA =(('perro','perro'),('gato','gato'))
    idmas = models.AutoField(primary_key=True)
    Cliente = models.ForeignKey(Cliente,related_name='dueño', on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sexo = models.CharField(max_length=50, choices=SEXO, blank=True, null=True)
    tipo_mascota = models.CharField(max_length=50,choices=TMASCOTA, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    pash = models.ManyToManyField(Paseador,blank=True)
    foto =models.ImageField(upload_to="mascotas",blank=True)

    def __str__(self):
        return self.nombre
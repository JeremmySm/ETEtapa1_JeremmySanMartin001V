from django.db import models

# Create your models here.

#Modelo para usuario
class Pais(models.Model):
    idpais      = models.IntegerField   (primary_key=True, verbose_name='Id de pais')
    nombrepais  = models.CharField      (max_length=50, verbose_name='Nombre del país')
    def __int__(self):

        return self.idpais


class Proveedor(models.Model):
    idproveedor = models.IntegerField   (primary_key=True, verbose_name='Id de proveedor')
    foto        = models.ImageField     (upload_to='Proveedores', null=True)
    nombre_completo = models.CharField  (max_length=60, verbose_name='Nombre Completo')
    telefono    = models.CharField      (max_length=12, verbose_name='telefono')
    direccion   = models.CharField      (max_length=100, verbose_name='direccion')
    email       = models.CharField      (max_length=60, verbose_name='email')
    contrasena  = models.CharField      (max_length=15, verbose_name='contraseña')
    monedapago  = models.CharField      (max_length=10, verbose_name='tipo de moneda de pago')
    pais        = models.ForeignKey     (Pais, on_delete=models.CASCADE)
    def __int__(self):

        return self.idproveedor
 
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

from .authentication import CustomUserManager
import uuid

import qrcode
from io import BytesIO
from django.core.files import File
import json





# Create your models here.
class Usuario(AbstractUser):    
    username = None                                                                                                                                                                                                                                                                                                                                    
    nombre = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField()
    ROLES = (
        (1, "Administrador"),
        (2, "Bartender"),
        (3, "Mesero"),
        (4, "Cliente"),
    )
    rol = models.IntegerField(choices=ROLES, default=4)
    ESTADO = (
        (1, "Activo"),
        (2, "Bloqueado"),
    )
    estado = models.IntegerField(choices=ESTADO, default=1)
    foto = models.ImageField(upload_to="Img_usuarios/", default="Img_usuarios/default.png", blank=True)
    token_recuperar = models.CharField(max_length=254, default="", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "cedula", "fecha_nacimiento"]
    objects = CustomUserManager()


    def __str__(self):
        return self.nombre
    

class Bloqueo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="bloqueos")
    motivo = models.TextField()
    fecha_bloqueo = models.DateTimeField(auto_now_add=True)
    realizado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name="bloqueos_realizados")
    
    def __str__(self):
        return self.usuario.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    fecha = models.DateField()
    hora_incio = models.TimeField() 
    descripcion = models.TextField()
    aforo = models.IntegerField(default=500)
    entradas_disponibles = models.IntegerField(default=500)
    precio_entrada = models.IntegerField(default=50000)
    precio_vip = models.IntegerField(default=75000)
    reservas = models.BooleanField(default=False)
    entradas = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="Img_eventos/", default="Img_eventos/default.png")
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
@receiver(post_save, sender=Evento)
def actualizar_entradas_disponibles(sender, instance, created, **kwargs):
    if created:
        instance.entradas_disponibles = instance.aforo
        instance.save()
    
class CompraEntrada(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    entrada_general = models.IntegerField(default=1)
    entrada_vip = models.IntegerField(default=1)
    total = models.IntegerField(default=0)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


class EntradasQR(models.Model):
    compra = models.ForeignKey(CompraEntrada, on_delete=models.CASCADE, default=None)
    codigo_qr = models.CharField(max_length=100, unique=True)
    qr_imagen = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    estado_qr = models.BooleanField(default=True)
    tipo_entrada = models.CharField(max_length=10, default="General")

    def __str__(self):
        return f'{self.id}'
    
    def save(self, *args, **kwargs):
        if not self.codigo_qr:
            self.codigo_qr = str(uuid.uuid4())

        qr_data = {
            'tipo': 'entrada',
            'evento_nombre': self.compra.evento.nombre,
            'evento_foto': self.compra.evento.foto.url,
            'evento_fecha': self.compra.evento.fecha.strftime('%Y-%m-%d'),
            'evento_estado': self.compra.evento.estado,
            'usuario_nombre': self.compra.usuario.nombre,
            'usuario_email': self.compra.usuario.email,
            'usuario_cc': self.compra.usuario.cedula,
            'codigo_entrada': self.codigo_qr,
            'estado_qr': self.estado_qr,
            'tipo_entrada': self.tipo_entrada
        }
        
        qr_data_json = json.dumps(qr_data)
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_data_json)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'qr_{self.codigo_qr}.png'
        self.qr_imagen.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)


class Mesa(models.Model):
    ACTIVA = 'Activa'
    DISPONIBLE = 'Disponible'

    ESTADO_CHOICES = (
        (ACTIVA, 'Activa'),
        (DISPONIBLE, 'Disponible'),
    )

    RESERVADA = 'Reservada'
    DISPONIBLE = 'Disponible'

    RESERVA_CHOICES = (
        (RESERVADA, 'Reservada'),
        (DISPONIBLE, 'Disponible'),
    )
    nombre = models.CharField(max_length=300)
    capacidad = models.IntegerField(default=5)
    precio = models.IntegerField(default=1000000)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default=DISPONIBLE)
    estado_reserva = models.CharField(max_length=10, choices=RESERVA_CHOICES , default=DISPONIBLE)
    codigo_qr = models.CharField(max_length=100, unique=True)
    qr_imagen = models.ImageField(upload_to='mesas_qr_codes/', blank=True, null=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True, default=None)
    total_ganancia = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if not self.codigo_qr:
            self.codigo_qr = str(uuid.uuid4())
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(self.codigo_qr)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'qr_{self.codigo_qr}.png'
        self.qr_imagen.save(file_name, File(buffer), save=False)

        
        super().save(*args, **kwargs)

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    evento = models.ForeignKey(Evento, on_delete=models.DO_NOTHING)
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    codigo_qr = models.CharField(max_length=100, unique=True)
    qr_imagen = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    estado_qr = models.BooleanField(default=True)
    def __str__(self):
        return f'Mesa: {self.mesa} - Evento: {self.evento.nombre}'

    def save(self, *args, **kwargs):
        if not self.codigo_qr:
            self.codigo_qr = str(uuid.uuid4())

        qr_data = {
            'tipo': 'reserva',
            'evento_foto': self.evento.foto.url,
            'evento_nombre': self.evento.nombre,
            'evento_fecha': self.evento.fecha.strftime('%Y-%m-%d'),
            'evento_estado': self.evento.estado,
            'usuario_nombre': self.usuario.nombre,
            'usuario_email': self.usuario.email,
            'usuario_cc': self.usuario.cedula,
            'nombre_mesa': self.mesa.nombre,
            'capacidad_mesa': self.mesa.capacidad,
            'codigo_reserva': self.codigo_qr,
            'estado_qr': self.estado_qr
        }
        
        qr_data_json = json.dumps(qr_data)
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_data_json)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'qr_{self.codigo_qr}.png'
        self.qr_imagen.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)

class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="Img_categorias/", default="Img_categorias/default.png")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    inventario = models.IntegerField(default=0)
    foto = models.ImageField(upload_to="Img_productos/", default="Img_productos/default.png")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    comentario = models.TextField(default="")
    PREPARACION = 'En preparación'
    ENTREGADO = 'Entregado'
    CANCELADO = 'Cancelado'

    ESTADO_CHOICES = (
        (PREPARACION, 'En preparacion'),
        (ENTREGADO, 'Entregado'),
        (CANCELADO, 'Cancelado')
    )

    estado = models.CharField(max_length=14, choices=ESTADO_CHOICES, default=PREPARACION)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f'Pedido {self.id} - Mesa {self.mesa.nombre}'


class DetallePedido(models.Model):
    ACTIVO = 'Activo'
    ELIMINADO = 'Eliminado'
    ESTADO_CHOICES = (
        (ACTIVO, 'Activo'),
        (ELIMINADO, 'Eliminado')
    )

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default=ACTIVO)
    motivo_eliminacion = models.TextField(blank=True, default='')

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'


class HistorialPedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    PAGADO = 'Pagado'
    CANCELADO = 'Cancelado'

    ESTADO_CHOICES = (
        (PAGADO, 'Pagado'),
        (CANCELADO, 'Cancelado')
    )
    estado = models.CharField(max_length=14, choices=ESTADO_CHOICES, default=PAGADO)
    total = models.IntegerField()

    def __str__(self):
        return f'Historial Pedido {self.id} - Mesa {self.mesa.nombre}'

class HistorialDetallePedido(models.Model):
    historial_pedido = models.ForeignKey(HistorialPedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

class Galeria(models.Model):
    nombre = models.CharField(max_length=254)
    fecha = models.DateField()
    foto = models.ImageField(upload_to="Img_carpeta/", default="Img_carpeta/default.png")


class Fotos(models.Model):
    foto = models.ImageField(upload_to="Img_galeria/", default="Img_galeria/default.png")
    carpeta = models.ForeignKey(Galeria, on_delete=models.DO_NOTHING)

class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    total_ganancia = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    ESTADOS = (
        (1, 'Pendiente'),
        (2, 'Enviado'),
        (3, 'Rechazada'),
    )
    estado = models.IntegerField(choices=ESTADOS, default=1)

    def __str__(self):
        return f"{self.id} - {self.usuario}"



class DetalleVenta(models.Model):
	venta = models.ForeignKey(Venta, on_delete=models.DO_NOTHING)
	producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
	cantidad = models.IntegerField()
	precio_historico = models.IntegerField()

	def __str__(self):
		return f"{self.id} - {self.venta}"

"""
# ---------------------------------------------------------------------------------
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
"""

from .models import *

from rest_framework import serializers


# Serializers define the API representation.
class UsuarioSerializer(serializers.HyperlinkedModelSerializer, serializers.ModelSerializer):
    foto = serializers.ImageField(required=False)
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'password', 'cedula', 'fecha_nacimiento', 'rol', 'estado', 'foto', 'token_recuperar']

class BloqueoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bloqueo
        fields = ['id', 'usuario', 'motivo', 'fecha_bloqueo', 'realizado_por']

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fecha', 'hora_incio', 'descripcion', 'aforo', 'entradas_disponibles','precio_entrada', 'precio_vip', 'reservas','foto']

class CompraEntradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompraEntrada
        fields = ['id', 'usuario', 'evento', 'entrada_general', 'entrada_vip', 'total', 'fecha_compra']

class MesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mesa
        fields = ['id', 'nombre', 'capacidad', 'precio', 'estado', 'estado_reserva', 'codigo_qr']

class EntradasQRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EntradasQR
        fields = ['id', 'compra', 'codigo_qr', 'qr_imagen', 'estado_qr', 'tipo_entrada']


class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        #Agregar el 'usuario' cuando funcione
        fields = ['id', 'evento', 'mesa', 'fecha_compra', 'total', 'codigo_qr', 'qr_imagen']

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'foto']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'foto', 'categoria', 'precio']

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'usuario', 'fecha','comentario', 'estado', 'total']

class DetallePedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetallePedido
        fields = ['id', 'pedido', 'producto', 'cantidad', 'precio']

"""class InventarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'cantidad', 'fecha_caducidad']"""

class GaleriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galeria
        fields = ['id', 'nombre', 'fecha', 'foto']

class FotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fotos
        fields = ['id', 'foto', 'carpeta']

class VentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venta
        #Agregar el 'usuario' cuando funcione
        fields = ['fecha_venta', 'estado']

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ['venta', 'producto', 'cantidad', 'precio_historico']
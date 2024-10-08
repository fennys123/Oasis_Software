from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','cedula','fecha_nacimiento','email','password','rol','estado','foto','last_login']
    search_fields = ['id','nombre','cedula','email','telefono','rol','estado']
    list_filter = ['rol']
    list_editable = ['rol','estado']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")
    
@admin.register(Bloqueo)
class BloqueoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario', 'motivo', 'fecha_bloqueo', 'realizado_por']

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'nombre_plural', 'fecha', 'hora_incio', 'descripcion', 'aforo', 'entradas_disponibles', 'precio_entrada', 'precio_vip' , 'reservas', 'entradas','foto']
    search_fields = ['id','nombre','fecha','hora_incio']
    list_filter = ['fecha']
    list_editable = ['nombre','fecha','hora_incio', 'reservas', 'entradas', 'entradas_disponibles']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")

    def nombre_plural(self, obj):
        return mark_safe(f"<span style='color:red'>{obj.nombre}'s<span>")

@admin.register(CompraEntrada)
class CompraEntradaAdmin(admin.ModelAdmin):
    list_display = ['id','usuario', 'evento', 'entrada_general', 'entrada_vip', 'total', 'fecha_compra']
    search_fields =['id','usuario','evento','fecha_compra']
    list_editable = ['entrada_general', 'entrada_vip', 'total']

@admin.register(EntradasQR)
class entradasQRAdmin(admin.ModelAdmin):
    list_display = ['id', 'compra', 'codigo_qr', 'qr_imagen', 'estado_qr', 'tipo_entrada']


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'capacidad', 'precio','estado','estado_reserva','codigo_qr', 'usuario']
    search_fields = ['id','estado', 'capacidad','estado_reserva']
    list_filter = ['estado', 'capacidad','estado_reserva']
    list_editable = ['estado', 'capacidad', 'estado_reserva', 'precio']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario','evento','mesa','fecha_compra','total','codigo_qr', 'qr_imagen', 'estado_qr']
    search_fields =['id','usuario','evento','mesa','fecha_compra']
    list_filter = ['evento','fecha_compra']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion', 'foto']
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','inventario','precio','ver_foto']
    search_fields = ['id','nombre', 'precio']
    list_editable = ['precio']

    def ver_foto(self, obj):
        if obj.foto:
            return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='15%'></a>")
        

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','mesa','usuario', 'fecha','comentario','estado','total']
    search_fields = ['id','mesa','estado']
    list_filter = ['estado']
    list_editable = ['estado']

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['id','pedido','producto','cantidad', 'estado','precio'] 
    search_fields = ['id','pedido','producto','cantidad']
    list_filter = ['pedido']

@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ['id','mesa','usuario', 'fecha','estado','total']
    search_fields = ['id','mesa','estado']
    list_filter = ['estado']
    list_editable = ['estado']

@admin.register(HistorialDetallePedido)
class HistorialDetallePedidoAdmin(admin.ModelAdmin):
    list_display = ['id','historial_pedido','producto', 'cantidad','precio']

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'fecha', 'foto', 'ver_foto']
    search_fields = ['nombre', 'fecha', 'foto']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")

@admin.register(Fotos)
class FotosAdmin(admin.ModelAdmin):
    list_display = ['foto', 'carpeta', 'ver_foto']
    search_fields = ['foto', 'carpeta']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='10%'></a>")


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    #Agregar 'usuario' cuando funcione
    list_display = ['id', 'usuario','fecha_venta']

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ['id', 'venta', 'producto', 'cantidad', 'precio_historico', 'subtotal']

    def subtotal(self, obj):
        return f"{obj.cantidad * obj.precio_historico}"
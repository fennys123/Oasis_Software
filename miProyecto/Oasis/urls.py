from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as especial

from . import views


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'evento', views.EventoViewSet)
router.register(r'mesa', views.MesaViewSet)
router.register(r'reserva', views.ReservaViewSet)
router.register(r'categoria', views.CategoriaViewSet)
router.register(r'producto', views.ProductoViewSet)
router.register(r'pedido', views.PedidoViewSet)
router.register(r'detalle_pedido', views.DetallePedidoViewSet)
router.register(r'compra_entrada', views.CompraEntradaViewSet)
#router.register(r'inventario', views.InventarioViewSet)
router.register(r'galeria', views.GaleriaViewSet)
router.register(r'fotos', views.FotosViewSet)
router.register(r'venta', views.VentaViewSet)
router.register(r'detalle_venta', views.DetalleVentaViewSet)


urlpatterns = [
    
    path('api/1.0/', include(router.urls)),
    path('api/1.0/token-auth/', views.CustomAuthToken.as_view()),
	path('api/1.0/api-auth/', include('rest_framework.urls')),
	path('api/1.0/token_qr/<str:mesa>/', views.token_qr_movil.as_view()),
    path('api/1.0/comprar_entradas/', views.comprar_entradas_movil.as_view()),
    path('api/1.0/entradas_usuario/<int:id>/', views.entradas_usuario_movil.as_view()),
    path('api/1.0/entradas_detalles_usuario/<int:user_id>/<int:entrada_id>/', views.entradas_detalles_usuario_movil.as_view()),
    path('api/1.0/mesas_reservadas/<int:id_evento>/', views.mesas_reservadas_movil.as_view()),
    path('api/1.0/reservar_mesa/', views.reservar_mesa_movil.as_view()),
    path('api/1.0/reservas_usuario/<int:id>/', views.reservas_usuario_movil.as_view()),
    path('api/1.0/reservas_detalles_usuario/<int:user_id>/<int:reserva_id>/', views.reservas_detalles_usuario_movil.as_view()),
    path('api/1.0/realizar_pedido/', views.realizar_pedido_movil.as_view()),
    path('api/1.0/pedidos_usuario/<int:user_id>/', views.ver_pedido_usuario_movil.as_view()),
    path('api/1.0/eliminar_pedido_usuario/<int:id_pedido>/', views.eliminar_pedido_usuario_movil.as_view()),
    path('api/1.0/eliminar_producto_pedido_usuario/<int:id_detalle>/', views.eliminar_producto_pedido_usuario_movil.as_view()),
    path('api/1.0/pagar_pedido_usuario/<int:id_usuario>/<str:codigo_mesa>/', views.pagar_pedido_usuario_movil.as_view()),
    path('api/1.0/liberar_mesa_usuario/<str:codigo_mesa>/', views.liberar_mesa_usuario_movil.as_view()),
    path('api/1.0/verificar_pedido_usuario/<int:id_usuario>/', views.verificar_pedido_usuario_movil.as_view()),
    path('api/1.0/pedidos_mesa/<str:codigo_mesa>/', views.ver_pedido_mesa_movil.as_view()),
    path('api/1.0/pedidos_mesa_cargo/<int:id_usuario>/', views.ver_mesa_cargo_movil.as_view()),
    path('api/1.0/reserva_escaneado/<str:codigo_qr>/', views.qr_reserva_escaneado_movil.as_view()),
    path('api/1.0/entrada_escaneado/<str:codigo_qr>/', views.qr_entrada_escaneado_movil.as_view()),
    path('api/1.0/categoria_productos/<int:id_categoria>/', views.categoria_productos_movil.as_view()),
    path('api/1.0/galeria_fotos/<int:id_carpeta>/', views.galeria_fotos_movil.as_view()),
    path('api/1.0/registrar_usuario/', views.registrar_usuario_movil.as_view()),




    path('', views.index, name="index"),
	path('inicio/', views.inicio, name="inicio"),


    #Autenticación de usuarios del sistema
    path('register/', views.crear_usuario_registro, name="usuario_registro"),
    path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),


    path('form_recuperar_contrasena/', views.recuperar_contrasena_template, name='form_recuperar_contrasena'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('verificar_recuperar/', views.verificar_recuperar, name='verificar_recuperar'),
    path('registro/', views.registro, name='registro'),

    #TÉRMINOS Y CONDICIONES
    path('tyc/', views.terminos_condiciones, name='tyc'),


    #PERFIL
    path('Perfil/', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/<int:id>/', views.editar_perfil, name='editar_perfil'),
    path('entradas/', views.entradas_usuario, name='entradas_usuario'),
    path('entradas_info/<int:id>/', views.entradas_usuario_info, name='entrada_info'),
    path('reservas/', views.reservas_usuario, name='reservas_usuario'),
    path('reservas_info/<int:id>/', views.reservas_usuario_info, name='reserva_info'),

    path('ver_mesas_a_cargo/', views.ver_mesas_a_cargo, name='ver_mesas_a_cargo'),



    #CAMBIAR CONTRASEÑA
    path('cambiar_clave/', views.cambiar_clave, name="cambiar_clave"),


    #USUARIOS
    path('Gestion_Usuarios/', views.guInicio, name='guInicio'),
    path('Usuarios_Eliminados/<int:id>', views.guUsuariosEliminados, name='guUsuariosEliminados'),
    path('Usuarios_Actualizar/<int:id>', views.guUsuariosActualizar, name='guUsuariosActualizar'),
    path('guUsuariosCrear/', views.guUsuariosCrear, name='guUsuariosCrear'),
    
    path('gu_reservas_usuario/<int:id>', views.gu_reservas_usuario, name='gu_reservas_usuario'),
	path("gu_historial_pedidos/<int:id>", views.gu_historial_pedidos_usuario, name="gu_historial_pedidos_usuario"),


    path('Usuarios_Bloqueados/', views.guUsuariosBloqueados, name='guUsuariosBloqueados'),
    path('Bloquear_Usuario/<int:id>', views.guBloquearUsuario, name='guBloquearUsuario'),
    path('Desbloquear_Usuario/<int:id>', views.guDesbloquearUsuario, name='guDesbloquearUsuario'),


    #CRUD INVENTARIO
    #path('Gestion_Inventario/', views.invInicio, name='inventario'),
    #path('Agregar_Producto/', views.invForm, name='invForm'),
    #path('Crear_Inventario/', views.crearInventario, name='crearInventario'),
    #path('Eliminar_Inventario/<int:id>', views.eliminarInventario, name='eliminarInventario'),
    #path('Inventario_Actualizar/<int:id>', views.invFormActualizar, name='invFormActualizar'),
    #path('Actualizar_Inventario/', views.actualizarInventario, name='actualizarInventario'),


    #CRUD PRODUCTOS
    path('Gestion_Productos/', views.invProductos, name='Productos'),
    path('Crear_Producto/', views.crearProducto, name='crearProducto'),
    path('Eliminar_Producto/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('Actualizar_Producto/<int:id>', views.actualizarProducto, name='actualizarProducto'),
    path('Inv_Detalle_Producto/<int:id>', views.invDetalleProducto, name='invDetalleProducto'),



    #PEDIDOS
    path('Gestion_Pedidos/', views.peInicio, name='peInicio'),
    path('Historial_Pedidos/', views.ver_historial_pedidos, name='peHistorial'),
    path('Mesas/', views.peGestionMesas, name='peGestionMesas'),
    path('Agregar_Pedido/<int:id>', views.pedidoEmpleado, name='pedidoEmpleado'),
	path("crear_pedido/<int:id>", views.crear_pedido_admin, name="crear_pedido_admin"),

    #PEDIDOS USUARIO
    path('escanear_mesa/', views.escanear_mesa, name='escanear_mesa'),
    path('pedidoUsuario/<int:id>/', views.pedidoUsuario, name='pedidoUsuario'),
    path('crear_pedido_usuario/<int:id>', views.crear_pedido_usuario, name='crear_pedido_usuario'),



    #CRUD MESAS
    path('Gestion_Mesas/', views.mesaInicio, name='Mesas'),
    path('Agregar_Mesa/', views.crearMesa, name='crearMesa'),
    path('Actualizar_Mesa/<int:id>', views.mesaActualizar, name='mesaActualizar'),
    path('Eliminar_Mesa/<int:id>', views.eliminarMesa, name='eliminarMesa'),

    path('reservasMesa/<int:id>', views.reservasMesa, name='reservasMesa'),

    path('reporte-mesas/', views.reporte_mesas, name='reporte_mesas'),
    path('limpiar_ganancias/<int:mesa_id>/', views.limpiar_ganancias, name='limpiar_ganancias'),
    path('limpiar-todas-ganancias/', views.limpiar_todas_ganancias, name='limpiar_todas_ganancias'),



#   CRUD EVENTOS
    path('Gestion_Eventos/', views.eveInicio, name='Eventos'),
    path('Agregar_Evento/', views.crearEvento, name='crearEvento'),
    path('Eliminar_Evento/<int:id>', views.eliminarEvento, name='eliminarEvento'),
    path('Actualizar_Evento/<int:id>', views.actualizarEvento, name='actualizarEvento'),
    path('Reservas/<int:id>', views.eveReserva, name='eveReserva'),
    path('ReservasLLegada/<str:codigo_qr>', views.eveReservaLlegada, name='eveReservaLlegada'),
    path('Evento_Entradas/<int:id>', views.eveEntradas, name='eveEntradas'),
    path('Eliminar_Entrada/<int:id>', views.eliminarEntrada, name='eliminarEntrada'),

    path('Detalle_Evento/<int:id>', views.detalleEvento, name='detalleEvento'),

    path('Gestion_Eventos_Eliminados/', views.eveEliminados, name='EventosEliminados'),
    path('Eliminar_Evento_Definitivo/<int:id>', views.eliminarEventoDefinitivo, name='eliminarEventoDefinitivo'),



#   CRUD MENÚ (CATEGORÍAS)
    path('Gestion_Menu/', views.meInicio, name='Menu'),
    path('Crear_Categoria/', views.crearCategoria, name='crearCategoria'),
    path('Eliminar_Categoria/<int:id>', views.eliminarCategoria, name='eliminarCategoria'),
    path('Actualizar_Categoria/<int:id>', views.actualizarCategoria, name='actualizarCategoria'),
    path('Productos/<int:id>', views.meProductos, name='meProductos'),
    path('Me_Crear_Producto/<int:id>', views.meCrearProducto, name='meCrearProducto'),
    path('Me_Detalle_Producto/<int:id>', views.meDetalleProducto, name='meDetalleProducto'),


#   CRUD GALERÍA
    path('Gestion_Galeria/', views.gaInicio, name='gaInicio'),
    path('Agregar_Carpeta/', views.crearCarpeta, name='crearCarpeta'),
    path('Eliminar_Carpeta/<int:id>', views.eliminarCarpeta, name='eliminarCarpeta'),
    path('Actualizar_Carpeta/<int:id>', views.actualizarCarpeta, name='actualizarCarpeta'),
    path('Galeria_Fotos/<int:id>', views.gaFotos, name='gaFotos'),
    path('gaAgregarFoto/<int:id>', views.agregarFoto, name='agregarFoto'),
    path('eliminarFoto/<int:id>', views.eliminarFoto, name='eliminarFoto'),
    path('CambiarFoto/<int:id>', views.cambiarFoto, name='cambiarFoto'),



#   FRONT PRODUCTOS
    path('front_productos/', views.front_productos, name='front_productos'),
    path('front_producto_info/<int:id>', views.front_producto_info, name='front_producto_info'),

#   FRONT EVENTOS
    path('front_eventos/', views.front_eventos, name='front_eventos'),
    path('front_eventos_info/<int:id>/', views.front_eventos_info, name='front_eventos_info'),

#   FRONT GALERIA
    path('front_galeria/', views.front_galeria, name='front_galeria'),
    path('front_fotos/<int:id>', views.front_fotos, name='front_fotos'),


# CARRITO DE COMPRA USUARIO
	path("carrito_add/", views.carrito_add, name="carrito_add"),
	path("carrito_ver/", views.carrito_ver, name="carrito_ver"),
    path("carrito_eliminar/<int:id>/", views.carrito_eliminar, name="carrito_eliminar"),
	path("vaciar_carrito/", views.vaciar_carrito, name="vaciar_carrito"),
	path("actualizar_totales_carrito/<int:id_producto>/", views.actualizar_totales_carrito, name="actualizar_totales_carrito"),

#CARRITO DE COMPRA MESERO
	path("carrito_ver_admin/", views.carrito_ver_admin, name="carrito_ver_admin"),
	path("actualizar_totales_carrito_admin/<int:id_producto>/", views.actualizar_totales_carrito_admin, name="actualizar_totales_carrito_admin"),
    path("carrito_eliminar_admin/<int:id>/", views.carrito_eliminar_admin, name="carrito_eliminar_admin"),
	path("vaciar_carrito_admin/", views.vaciar_carrito_admin, name="vaciar_carrito_admin"),
    
    path('ver_pedidos_mesa/<int:mesa_id>/', views.ver_pedidos_mesa, name='ver_pedidos_mesa'),

    path('pagar_pedido/<int:id>/<str:rol>/', views.pagar_pedido, name='pagar_pedido'),
    path('entregar_pedido/<int:id>/', views.entregar_pedido, name='entregar_pedido'),

    path('cancelar_pedido/', views.cancelar_pedido, name='cancelar_pedido'),
    path('cancelar_pedido_sin_comentario/<int:id_pedido>/<str:ruta>/', views.cancelar_pedido_sin_comentario, name='cancelar_pedido_sin_comentario_sin_mesa'),
    path('cancelar_pedido_sin_comentario/<int:id_pedido>/<int:id_mesa>/<str:ruta>/', views.cancelar_pedido_sin_comentario, name='cancelar_pedido_sin_comentario'),


    path('eliminar_producto/', views.eliminar_item, name='eliminar_producto'),
    path('eliminar_producto_sin_comentario/<int:id_producto>/<str:ruta>/', views.eliminar_item_sin_comentario, name='eliminar_item_sin_comentario_sin_mesa'),
    path('eliminar_producto_sin_comentario/<int:id_producto>/<int:id_mesa>/<str:ruta>/', views.eliminar_item_sin_comentario, name='eliminar_item_sin_comentario'),

    path('liberar_mesa/<int:id>/', views.liberar_mesa, name='liberar_mesa'),




#VENTAS
	path("crear_venta/", views.crear_venta, name="crear_venta"),
	path("historial_pedidos/", views.ver_pedidos_usuario, name="ver_ventas"),
	path("ver_detalles_pedido_usuario/", views.ver_detalles_usuario, name="ver_detalles_pedido_usuario"),

#COMPRAR ENTRADAS
    path("comprar_entradas/<int:id>/", views.comprar_entradas, name="comprar_entradas"),

#RESERVAR MESAS
    path("reservar_mesa/<int:id>/", views.reservar_mesa, name="reservar_mesa"),
    path("eliminar_reserva/<int:id>/", views.eliminar_reserva, name="eliminar_reserva"),

#MOSTRAR TOTAL DE GANANCIAS
    path("ganancia_total/", views.ganancia_total, name="ganancia_total"),
    path('descargar_pdf_ganancias/<int:id>/', views.descargar_pdf_ganancias, name='descargar_pdf_ganancias'),

#mas_info
    path("mas_info/", views.mas_info, name="mas_info"),
]   
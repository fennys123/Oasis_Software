function eliminar(url){
    if (confirm('Está seguro?')){
        location.href = url;
    }
}

function remove_producto(url){
    location.href = url;
}

function ver_carrito_admin(url, template_name){
    let csrf_token_element = $("[name='csrfmiddlewaretoken']")[0];
    if (!csrf_token_element) {
        alert("CSRF token not found");
        return;
    }
    let csrf_token = csrf_token_element.value;


    contenido = $("#respuesta_carrito")


    offCanvas_carrito = $("#carritoCompras");
    offCanvas_carrito.offcanvas('toggle');

    $.ajax({
        url: url,
        type: "POST",
        data: {
            "csrfmiddlewaretoken": csrf_token, 
            "template_name": template_name,
        }
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/pedidos/pedidoEmpleado/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/pedidos/pedidoEmpleado/";
    });
}


function add_carrito_admin(url, id_producto, template_name){
    let csrf_token_element = $("[name='csrfmiddlewaretoken']")[0];
    if (!csrf_token_element) {
        alert("CSRF token not found");
        return;
    }
    let csrf_token = csrf_token_element.value;

    let id = $(`#id_${id_producto}`).val();
    let cantidad = $(`#cantidad_${id_producto}`).val();

    let contenido = $("#respuesta_carrito");

    $.ajax({
        url: url,
        type: "POST",
        data: {
            "csrfmiddlewaretoken": csrf_token, 
            "id": id, 
            "cantidad": cantidad,
            "template_name": template_name,
        }
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta);
        }
        else{
            location.href="/Oasis/pedidos/pedidoEmpleado/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/pedidos/pedidoEmpleado/";
    });
}

function carrito_eliminar_admin(url){
    contenido = $("#respuesta_carrito")

    $.ajax({
        url: url,
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/pedidos/pedidoEmpleado/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/pedidos/pedidoEmpleado/";
    });
}


function actualizar_totales_carrito_admin(url,id){
    contenido = $("#respuesta_carrito")
    cantidad = $("#cantidad_carrito_"+id)
    
    $.ajax({
        url: url,
        type: "GET",
        data: {"cantidad": cantidad.val()}
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/pedidos/pedidoEmpleado/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/pedidos/pedidoEmpleado/";
    });
}

function eliminar(url){
    if (confirm('Está seguro?')){
        location.href = url;
    }
}


function remove_producto(url){
    location.href = url;
}
document.addEventListener("DOMContentLoaded", function() {
    const selectMesa = document.getElementById('mesaSelect');
    const botonEscaneada = document.getElementById('escaneadaButton');

    function verificarSelect() {
        if (selectMesa.value === '') {
            botonEscaneada.disabled = true;
        } else {
            botonEscaneada.disabled = false;
        }
    }

    selectMesa.addEventListener('change', verificarSelect);

    verificarSelect();
});

function mesa_escaneada(url) {
    const mesaId = document.getElementById('mesaSelect').value;
    if (mesaId) {
        window.location.href = `${url}${mesaId}/`;
    }
}

function ver_carrito(url){
    contenido = $("#respuesta_carrito")
    $.ajax({
        url: url
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/escanear_mesa/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/escanear_mesa/";
    });
}


function add_carrito(url, id_producto){
    
    csrf_token = $("[name='csrfmiddlewaretoken']")[0].value;
    id = $(`#id_${id_producto}`).val()
    cantidad = $(`#cantidad_${id_producto}`).val()

    contenido = $("#respuesta_carrito")

    $.ajax({
        url: url,
        type: "POST",
        data: {"csrfmiddlewaretoken": csrf_token, "id": id, "cantidad": cantidad}
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/escanear_mesa/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/escanear_mesa/";
    });
    
}

function carrito_eliminar(url){
    contenido = $("#respuesta_carrito")

    $.ajax({
        url: url,
    })
    .done(function(respuesta){
        if (respuesta != "Error"){
            contenido.html(respuesta)
        }
        else{
            location.href="/Oasis/escanear_mesa/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/escanear_mesa/";
    });
}


function actualizar_totales_carrito(url,id){
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
            location.href="/Oasis/escanear_mesa/";
        }
    })
    .fail(function(respuesta){
        location.href="/Oasis/escanear_mesa/";
    });
}



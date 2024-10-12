document.addEventListener("DOMContentLoaded", function() {
    function updateTotals() {
        const precioEntradaGeneralElement = document.getElementById('precio-entrada-general-oculto');
        const precioEntradaVipElement = document.getElementById('precio-entrada-vip-oculto');
        const cantidadEntradaGeneralElement = document.getElementById('entrada-general-cantidad');
        const cantidadEntradaVipElement = document.getElementById('entrada-vip-cantidad');
        
        if (precioEntradaGeneralElement && precioEntradaVipElement && cantidadEntradaGeneralElement && cantidadEntradaVipElement) {
            const precioEntradaGeneral = parseInt(precioEntradaGeneralElement.textContent);
            const precioEntradaVip = parseInt(precioEntradaVipElement.textContent);
            const cantidadEntradaGeneral = parseInt(cantidadEntradaGeneralElement.value);
            const cantidadEntradaVip = parseInt(cantidadEntradaVipElement.value);

            const totalEntradaGeneral = precioEntradaGeneral * cantidadEntradaGeneral;
            const totalEntradaVip = precioEntradaVip * cantidadEntradaVip;
            const totalGeneral = totalEntradaGeneral + totalEntradaVip;

            document.getElementById('precio-entrada-general').textContent = '$' + totalEntradaGeneral.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
            document.getElementById('precio-entrada-vip').textContent = '$' + totalEntradaVip.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
            document.getElementById('total-general').textContent = 'Total $' + totalGeneral.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
        }
    }

    const entradaGeneralCantidadElement = document.getElementById('entrada-general-cantidad');
    const entradaVipCantidadElement = document.getElementById('entrada-vip-cantidad');
    
    if (entradaGeneralCantidadElement && entradaVipCantidadElement) {
        entradaGeneralCantidadElement.addEventListener('change', updateTotals);
        entradaVipCantidadElement.addEventListener('change', updateTotals);
        entradaGeneralCantidadElement.addEventListener('input', verificarCantidades);
        entradaVipCantidadElement.addEventListener('input', verificarCantidades);
    }

    document.querySelector('.btn[data-bs-target="#confirmModal"]').addEventListener('click', function() {
        const cantidadGeneral = document.getElementById('entrada-general-cantidad').value;
        const precioGeneral = document.getElementById('precio-entrada-general').textContent;
        const cantidadVIP = document.getElementById('entrada-vip-cantidad').value;
        const precioVIP = document.getElementById('precio-entrada-vip').textContent;

        if (cantidadGeneral > 0) {
            document.getElementById('modal-entrada-general-cantidad').textContent = cantidadGeneral;
            document.getElementById('modal-entrada-general-precio').textContent = precioGeneral;
            document.getElementById('detalle-general').style.display = '';
        } else {
            document.getElementById('detalle-general').style.display = 'none';
        }

        if (cantidadVIP > 0) {
            document.getElementById('modal-entrada-vip-cantidad').textContent = cantidadVIP;
            document.getElementById('modal-entrada-vip-precio').textContent = precioVIP;
            document.getElementById('detalle-vip').style.display = '';
        } else {
            document.getElementById('detalle-vip').style.display = 'none';
        }

        document.getElementById('modal-total').textContent = document.getElementById('total-general').textContent;
    });

    function verificarCantidades() {
        const cantidadGeneral = document.getElementById('entrada-general-cantidad').value;
        const cantidadVip = document.getElementById('entrada-vip-cantidad').value;
        const botonComprar = document.getElementById('botonComprar');

        if (parseInt(cantidadGeneral) > 0 || parseInt(cantidadVip) > 0) {
            botonComprar.className = "btn btn-primary";
        } else {
            botonComprar.className = "btn btn-dark disabled";
        }
    }

    document.addEventListener('DOMContentLoaded', verificarCantidades);
    
    document.getElementById('confirmarCompraBtn').addEventListener('click', function() {
        const cantidadGeneral = document.getElementById('entrada-general-cantidad').value;
        const cantidadVIP = document.getElementById('entrada-vip-cantidad').value;
        const totalGeneral = document.getElementById('total-general').textContent;
        const eventoId = document.querySelector('#confirmarCompraBtn').getAttribute('data-evento-id');

        const datos = {
            cantidad_general: cantidadGeneral,
            cantidad_vip: cantidadVIP,
            total_general: totalGeneral
        };

        fetch(`http://127.0.0.1:8000/comprar_entradas/${eventoId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify(datos)
        })
        .then(response => response.json())
        .then(data => {
            const messagesDiv = document.getElementById('messages');
            data.messages.forEach(message => {
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('alert');
                if (message.message_type === 'success') {

                    // Cerrar el modal simulando el clic en el botón de cerrar
                    const closeModalButton = document.querySelector('#confirmModal .btn-close');
                    closeModalButton.click();

                    messageDiv.classList.add('alert-success');
                    alert(message.message);


                } else if (message.message_type === 'error') {
                    messageDiv.classList.add('alert-danger');
                    alert(message.message);
                } else if (message.message_type === 'warning') {
                    messageDiv.classList.add('alert-warning');
                    alert(message.message);
                }
                messageDiv.innerHTML = `
                <span>${message.message}</span>
                <button type="button" class="btn-close close-button" aria-label="Close"></button>
                `;
                messagesDiv.appendChild(messageDiv);

                const closeButton = messageDiv.querySelector('.btn-close');
                closeButton.addEventListener('click', () => {
                    messageDiv.remove();
                });
            });
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al procesar la solicitud' + error);
        });
    });

    document.querySelector('select[name="mesa"]').addEventListener('change', function() {
        verificarSelect();
        mostrarDetalleMesa();
    });

    function verificarSelect() {
        const selectMesa = document.querySelector('select[name="mesa"]');
        const botonReservar = document.getElementById('botonReservar');

        if (selectMesa.value === '') {
            botonReservar.className = "btn btn-dark disabled";
        } else {
            botonReservar.className = "btn btn-primary";
        }
    }

    function mostrarDetalleMesa() {
        const selectMesa = document.querySelector('select[name="mesa"]');
        const nombreMesaSeleccionada = document.getElementById('nombre-mesa-seleccionada');
        const capacidadMesaSeleccionada = document.getElementById('capacidad-mesa-seleccionada');
        const idMesaSeleccionada = document.getElementById('id-mesa-seleccionada');
        const totalReservaMesa = document.getElementById('total-reserva-mesa');
        const totalFrontReservaMesa = document.getElementById('total-front-reserva-mesa');

        const opcionSeleccionada = selectMesa.options[selectMesa.selectedIndex];
        const mesaNombre = opcionSeleccionada.dataset.nombre;
        const mesaCapacidad = opcionSeleccionada.dataset.capacidad;
        const mesaPrecio = parseFloat(opcionSeleccionada.dataset.precio);
        const entradaPrecio = parseFloat(opcionSeleccionada.dataset.entrada);
        const mesaId = selectMesa.value;

        const totalEntradas = entradaPrecio * mesaCapacidad;
        const total = mesaPrecio + totalEntradas;

        nombreMesaSeleccionada.textContent = mesaNombre;
        capacidadMesaSeleccionada.textContent = mesaCapacidad;
        idMesaSeleccionada.textContent = mesaId;
        totalReservaMesa.textContent = total;
        totalFrontReservaMesa.textContent = '$' + total.toLocaleString('es-CO', { style: 'decimal', minimumFractionDigits: 0, maximumFractionDigits: 0 });
    }

    verificarSelect();
    mostrarDetalleMesa();
});

function getCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
    return cookieValue;
}


document.getElementById('confirmarReservaBtn').addEventListener('click', function() {
    const selectMesa = document.querySelector('select[name="mesa"]');
    const mesaId = selectMesa.value;
    const totalGeneral = document.getElementById('total-reserva-mesa').textContent;
    const eventoId = document.querySelector('#confirmarReservaBtn').getAttribute('data-evento-id');

    const datos = {
        id_mesa: mesaId,
        total_general: totalGeneral
    };

    fetch(`http://127.0.0.1:8000/reservar_mesa/${eventoId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        const messagesDiv = document.getElementById('messages');
        data.messages.forEach(message => {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('alert');
            if (message.message_type === 'success') {

                // Cerrar el modal simulando el clic en el botón de cerrar
                const closeModalButton = document.querySelector('#confirmCompraMesa .btn-close');
                closeModalButton.click();

                messageDiv.classList.add('alert-success');
                alert(message.message);
            } else if (message.message_type === 'error') {
                messageDiv.classList.add('alert-danger');
                alert(message.message);
            } else if (message.message_type === 'warning') {
                messageDiv.classList.add('alert-warning');
                alert(message.message);
            }
            messageDiv.innerHTML = `
              <span>${message.message}</span>
              <button type="button" class="btn-close close-button" aria-label="Close"></button>
            `;
            messagesDiv.appendChild(messageDiv);

            const closeButton = messageDiv.querySelector('.btn-close');
            closeButton.addEventListener('click', () => {
                messageDiv.remove();
                location.reload();
            });
        }); 
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al procesar la solicitud' + error);
    });
});


function confirmarLimpiarGanancias(event) {
    event.preventDefault(); // Evita que el formulario se envíe inmediatamente
    const confirmar = confirm("¿Estás seguro de que deseas limpiar las ganancias de esta mesa?");
    if (confirmar) {
      event.target.closest("form").submit(); // Envía el formulario si el usuario confirma
    }
  }


// Función para agregar una nueva fila de producto
function agregarFila() {
    var tabla = document.getElementById("pedidoTabla").getElementsByTagName("tbody")[0];
    var nuevaFila = tabla.insertRow();

    // Crear celdas para producto y cantidad
    var celdaProducto = nuevaFila.insertCell(0);
    var celdaCantidad = nuevaFila.insertCell(1);
    var celdaAcciones = nuevaFila.insertCell(2);

    // Insertar inputs en las celdas
    celdaProducto.innerHTML = '<input type="text" name="producto[]" class="form-control" required>';
    celdaCantidad.innerHTML = '<input type="number" name="cantidad[]" class="form-control" required>';
    celdaAcciones.innerHTML = '<button type="button" class="btn btn-danger" onclick="eliminarFila(this)">Eliminar</button>';
}

// Función para eliminar una fila de la tabla
function eliminarFila(boton) {
    var fila = boton.parentNode.parentNode;
    fila.parentNode.removeChild(fila);
}
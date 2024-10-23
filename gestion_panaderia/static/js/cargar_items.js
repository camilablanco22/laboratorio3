document.getElementById('add-item').addEventListener('click', function(e) {
    e.preventDefault();

    // Asegurarse de que el campo formsetTotalForms existe
    var formsetTotalForms = document.getElementById('id_items_venta-TOTAL_FORMS');

    if (formsetTotalForms) {
        var totalForms = parseInt(formsetTotalForms.value);  // Leer el número total de formularios

        // Obtener el contenedor de formularios
        var formContainer = document.getElementById('item-formsnnnnnnnnnn b');

        // Clonar el primer formulario y limpiar sus valores
        var newForm = document.querySelector('.item-form').cloneNode(true);
        var formRegex = new RegExp(`items_venta-(\\d+)-`, 'g'); // Cambiar a tu nombre de formulario

        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `items_venta-${totalForms}-`);

        // Limpiar los valores del nuevo formulario
        newForm.querySelectorAll('input, select').forEach(function(input) {
            input.value = '';
        });

        // Agregar el nuevo formulario al contenedor
        formContainer.appendChild(newForm);

        // Incrementar el contador total de formularios
        formsetTotalForms.value = totalForms + 1;
    } else {
        console.error("No se encontró el campo TOTAL_FORMS");
    }
});


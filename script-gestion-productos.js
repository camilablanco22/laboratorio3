
function string_unidad(unidad_value){
    if(unidad_value==1){
        return "/Unid.";
    }else{
        return "/KG";
    }
}

function string_cantegoria(unidad_value){
    if(unidad_value==1){
        return "Panificación";
    }else{
        return "Pastelería";
    }
}


function guardar_producto(){
    let desc=document.getElementById('desc_producto').value;
    let precio=document.getElementById('precio').value;
    let precio_unidad_medida=string_unidad(document.getElementById('unidad_medida_precio').value);

    let cant_disponible = document.getElementById('cant_disponible').value;
    let cant_unidad_medida = string_unidad(document.getElementById('unidad_medida_cant').value);

    let categoria= string_cantegoria(document.getElementById('unidad_medida_cant').value);

    let cuerpo_tabla=document.getElementById('cuerpo-tabla');

    let fila_tabla=`<tr>
                              <th scope="row">1</th>
                              <td>${desc}</td>
                              <td>${categoria}</td>
                              <td>${cant_disponible} ${cant_unidad_medida}</td>
                              <td>$${precio} ${precio_unidad_medida}</td>
                              <td><button type="button" class="btn btn-dark btn-sm">Editar</button></td>
                              <td><button type="button" class="btn btn-dark btn-sm">Eliminar</button></td>
                            </tr>`
    cuerpo_tabla.innerHTML+=fila_tabla;


}


document.addEventListener('DOMContentLoaded', function (){
    document.getElementById('btn_guardar').addEventListener('click',function (event){
        event.preventDefault();
        guardar_producto();
    })
})
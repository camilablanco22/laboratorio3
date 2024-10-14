class Producto{
    constructor(descripcion, precio, precio_unidad, cant_disponible, cant_unidad_medida, categoría, ) {
        this.categoria=categoria;
        this.precio=precio;
        this.precio_unidad=precio_unidad;
        this.cant_disponible=cant_disponible;
        this.cant_unidad_medida=cant_unidad_medida;

    }

    modificar(categoría, precio, precio_unidad, cant_disponible, cant_unidad_medida){
        this.descripcion=descripcion;
        this.categoria=categoria;
        this.precio=precio;
        this.precio_unidad=precio_unidad;
        this.cant_disponible=cant_disponible;
        this.cant_unidad_medida=cant_unidad_medida;
    }
}



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

    productos.push(new Producto(desc, precio, precio_unidad_medida, cant_disponible, cant_unidad_medida, categoria ));

    actualizar_tabla();
}

function actualizar_tabla(){
    alert("actualiza")

    let cuerpo_tabla=document.getElementById('cuerpo-tabla');

    tabla.innerHTML=``
    productos.forEach(function (producto,index){

        let desc= producto.descripcion;
        let precio= producto.precio;
        let precio_unidad_medida= producto.precio_unidad_medida;
        let cant_disponible = producto.cant_disponible;
        let cant_unidad_medida= producto.cant_unidad_medida;
        let categoria = producto.categoria;
        let boton_editar = `<button type="button" id="btn_editar_${index}" class="btn btn-dark" onclick="modificar_producto(${index})">EDITAR</button>`
        let boton_eliminar = `<button type="button" id="btn_eliminar_${index}" class="btn btn-dark" onclick="eliminar_producto(${index})">ELIMINAR</button>`;


        let fila_tabla=`<tr>
                        <th scope="row">${index+1}</th>
                        <td>${desc}</td>
                        <td>${categoria}</td>
                        <td>${cant_disponible} ${cant_unidad_medida}</td>
                        <td>$${precio} ${precio_unidad_medida}</td>
                        <td>${boton_editar}</td>
                        <td>${boton_eliminar}</td>
                    </tr>`;
        cuerpo_tabla.innerHTML+=fila_tabla;
    })

}



document.addEventListener('DOMContentLoaded', function (){
    document.getElementById('btn_guardar').addEventListener('click',function (event){
        event.preventDefault();
        guardar_producto();
    })
})
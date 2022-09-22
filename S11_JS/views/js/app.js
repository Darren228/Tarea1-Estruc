$("#btnLogin").click(function(){
    $("#contenido").load("./router.php?action=login");
})
$("#btnRegistro").click(function(){
    alert("Ejecutando");
    $("#contenido").load("./router.php?action=registro");
})
$("#btnNuevo").click(function(){
    $.ajax({
        url:"./router.php?action=nuevoMensaje",
        type:"GET",
        dataType:"html",
        success: function(respuesta){
            $("#chatPersona").html(respuesta);
        }
    })
})

$("#btnSalir").click(function(){
    $.ajax({
        url:"./router.php?action=salir",
        type:"GET",
        dataType:"html",
        success: function(respuesta){
            $("#contenido").html(respuesta);
        }
    })
})

/**
 * Enviar por ajax el numero de telefono
 * Recibir el mensaje del controlador
 * 
 */




/**Funcion para utilizar ajax para esperar respuesta */
$("#frm_registro").submit(function(event){
    event.preventDefault();
    var parametros = $(this).serialize();
    $.ajax({
        url:"./router.php",
        type:"POST",
        dataType:"html",
        data:parametros,
        beforeSend:function(){
            $("#contenido").html("Procesando.... por favor espere")
        },
        success: function(respuesta){
            $("#contenido").html(respuesta);
        }
    })
});

$("#frm_login").submit(function(event){
    event.preventDefault();
    var parametros = $(this).serialize();
    $.ajax({
        url:"./router.php",
        type:"POST",
        dataType:"html",
        data:parametros,
        beforeSend:function(){
            $("#contenido").html("Procesando.... por favor espere")
        },
        success: function(respuesta){
            $("#contenido").html(respuesta);
        }
    })
});

$("#frm_enviarMensaje").submit(function(event){
    event.preventDefault();
    var parametros = $(this).serialize();
    $.ajax({
        url:"./router.php",
        type:"POST",
        dataType:"html",
        data:parametros,
        beforeSend:function(){
            $("#mensajes").html("Procesando.... por favor espere")
        },
        success: function(respuesta){
            $("#mensajes").html(respuesta);
            $("#texto").val('');
        }
    })
});

//Funciones llamadas
function cargarChat(obj){
    var parametros={
        "action":"cargarChat",
        "telefono":obj.id
    };
    $.ajax({
        url:"./router.php",
        type:"POST",
        dataType:"html",
        data:parametros,
        beforeSend:function(){
            $("#chatPersona").html("Procesando.... por favor espere")
        },
        success: function(respuesta){
            $("#chatPersona").html(respuesta);
        }
    })
}
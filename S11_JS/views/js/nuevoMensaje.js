var valido = true;
$("#idReceptor").blur(function(){
    //alert("Aca corresponde verificar si el numero de telefono existe y de quien");
    var parametros = $(this).serialize();
    idReceptor = document.getElementById("idReceptor").value;
    parametros={
        "action":"buscarReceptor",
        "idReceptor":idReceptor
    };
    $.ajax({
        url:"./router.php",
        type:"POST",
        dataType:"html",
        data:parametros,
        beforeSend:function(){
            $("#nombreReceptor").html("Procesando.... por favor espere")
        },
        success: function(respuesta){
            if(respuesta.length >1){
                $("#nombreReceptor").html(respuesta);
                $("#btnEnviarMensaje").removeAttr('disabled')
            }else{
                $("#nombreReceptor").html('Usuario no encontrado');
                $("#btnEnviarMensaje").attr("disabled","true");
            } 
        }
    })
})

$("#frm_nuevoMensaje").submit(function(event){
    event.preventDefault();
    var parametros = $(this).serialize();
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
});
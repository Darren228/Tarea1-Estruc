<?php
class Mensaje_controller{
    public function __construct(){}

    public static function insertar($datos,$chat){
        require_once './db.php';
        require_once './models/mensaje.php';
        require_once './models/usuario.php';
        $receptor = Usuario::buscarUsuario($datos['telefono']);
        $mensaje = new Mensaje($datos['idEmisor'],
            $receptor->getId(),$datos['texto']);
        Mensaje::insertar($mensaje);
        $mensajes = Mensaje::getMensajes($datos['idEmisor'],
            $receptor->getId());
        if($chat){
            require './views/mensaje/mensajes.php';
        }else{
            require './views/mensaje/chatPersona.php';
        } 
    }
    public static function cargarChat($datos){
        require_once './db.php';
        require_once './models/mensaje.php';
        require_once './models/usuario.php';
        $receptor = Usuario::buscarUsuario($datos['telefono']);
        $mensajes = Mensaje::getMensajes($datos['idEmisor'],
            $receptor->getId());
        require './views/mensaje/chatPersona.php';
    }
}


?>
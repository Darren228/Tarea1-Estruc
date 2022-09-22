<?php
class Usuario_controller{
    public function __construct(){}

    public static function insertar($datos){
        require_once './db.php';
        require_once './models/usuario.php';
        $nombre = $datos['nombre'];
        $telefono = $datos['telefono'];
        $clave = $datos['clave'];
        $usuario = new Usuario($telefono,$nombre);
        $usuario->setClave($clave);
        Usuario::insertar($usuario);
        Usuario_controller::iniciarSesion($datos);
    }
    
    public static function iniciarSesion($datos){
        require_once './db.php';
        require_once './models/usuario.php';
        $usuario = Usuario::iniciarSesion($datos['telefono'],$datos['clave']);
        if ($usuario){
            session_start();
            $_SESSION['id'] = $usuario->getId();
            $_SESSION['telefono'] = $usuario->getTelefono();
            $_SESSION['nombre'] = $usuario->getNombre();
            $personas = Usuario::getPersonas($_SESSION['id']);
            require './views/mensaje/chat.php';
        }else{
            echo "Error, Usuario y contrasena no valido";
            require './views/auth/login.php';
        }
    }
    public static function buscarUsuario($datos){
        require_once './db.php';
        require_once './models/usuario.php';
        $usuario = Usuario::buscarUsuario($datos['telefono']);
        if ($usuario){
            echo $usuario->getNombre();
        }else{
            echo "0";
        }
    }
}
?>
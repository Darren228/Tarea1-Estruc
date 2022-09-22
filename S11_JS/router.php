<?php
if(isset($_COOKIE['PHPSESSID'])){
    /**Acciones que se realizan cuando la sesion esta iniciada */
    session_start();
    if(isset($_POST['action'])){
        switch($_POST['action']){
            case 'enviarMensaje':{
                require_once './controllers/mensaje_controller.php';
                $datos['idEmisor'] = $_SESSION['id'];
                $datos['telefono'] = $_POST['idReceptor'];
                $datos['texto'] = $_POST['texto'];
                Mensaje_controller::insertar($datos,false);
                break;
            }
            case 'buscarReceptor':{
                require_once './controllers/usuario_controller.php';
                $datos['telefono'] = $_POST['idReceptor'];
                Usuario_controller::buscarUsuario($datos);
                break;
            }
            case 'cargarChat':{
                require_once './controllers/mensaje_controller.php';
                $datos['idEmisor'] = $_SESSION['id'];
                $datos['telefono'] = $_POST['telefono'];
                Mensaje_controller::cargarChat($datos);
                break;
            }
            case 'enviarMensajeChat':{
                require_once './controllers/mensaje_controller.php';
                $datos['idEmisor'] = $_SESSION['id'];
                $datos['telefono'] = $_POST['telefono'];
                $datos['texto'] = $_POST['texto'];
                Mensaje_controller::insertar($datos,true);
                break;
            }
        }
    }else if(isset($_GET['action'])){
        switch($_GET['action']){
            case 'nuevoMensaje':
                {require_once './views/mensaje/nuevoMensaje.php';
                break;}
            case 'salir':{
                echo "Cerrando sesion";
                session_start();
                session_destroy();
                setcookie("PHPSESSID","",time()-3600,"/");
                require './views/auth/login.php';
                break;
            }
        }
    }else{
        require './db.php';
        require './models/usuario.php';
        $personas = Usuario::getPersonas($_SESSION['id']);
        require_once './views/mensaje/chat.php';
    }
}else{
    if(isset($_POST['action'])){
        switch($_POST['action']){
            case 'iUsuario':
                {
                require_once './controllers/usuario_controller.php';
                $datos['nombre'] = $_POST['nombre'];
                $datos['telefono'] = $_POST['telefono'];
                $datos['clave'] = $_POST['clave'];
                Usuario_controller::insertar($datos);
                break;}
            case 'iniciarSesion':
            {
                    require_once './controllers/usuario_controller.php';
                    $datos['telefono'] = $_POST['telefono'];
                    $datos['clave'] = $_POST['clave'];
                    Usuario_controller::iniciarSesion($datos);
                    break;    
            }
        }
    }else if(isset($_GET['action'])){
        switch($_GET['action']){
            case 'login':
                require_once './views/auth/login.php';
                break;
            case 'registro':
                require_once './views/auth/registro.php';
                break;
        }
    }else{
        require_once './views/auth/login.php';
    }
}
?>
<?php
class Usuario{
    private $id;
    private $telefono;
    private $nombre;
    private $clave;

    function __construct($telefono, $nombre) {
        $this->telefono = $telefono;
        $this->nombre = $nombre;
    }
    function getId(){
        return $this->id;
    }
    function setId($id){
        $this->id = $id;
    }
    function getTelefono() {
        return $this->telefono;
    }

    function getNombre() {
        return $this->nombre;
    }

    function getClave() {
        return $this->clave;
    }

    function setTelefono($telefono): void {
        $this->telefono = $telefono;
    }

    function setNombre($nombre): void {
        $this->nombre = $nombre;
    }

    function setClave($clave): void {
        $this->clave = $clave;
    }

    public static function insertar($usuario){
        try{
            $pass = password_hash($usuario->getClave(),PASSWORD_DEFAULT);
            $db = Db::getConnect();
            $db->beginTransaction();
            $consulta = $db->prepare("INSERT INTO tbl_usuarios (telefono,nombre,clave)".
                " values (:telefono,:nombre,:clave)");
            $consulta->bindValue(':telefono',$usuario->getTelefono());
            $consulta->bindValue(':nombre',$usuario->getNombre());
            $consulta->bindValue(':clave',$pass);
            $consulta->execute();
            $db->commit();
        }catch(PDOException $e){
            $db->rollBack();
            echo "Se ha producido un error " . $e->getMessage();
            throw $e;
        }
    }
    public static function iniciarSesion($telefono,$clave){
        try{
            $db = Db::getConnect();
            $consulta = $db->prepare("SELECT * FROM tbl_usuarios where telefono=:telefono");
            $consulta->bindValue(':telefono',$telefono);
            $consulta->execute();
            $respuesta = $consulta->fetch();
            if($respuesta){
                if(password_verify($clave,$respuesta['clave'])){
                    $usuario = new Usuario($respuesta['telefono'],$respuesta['nombre']);
                    $usuario->setId($respuesta['id']);
                    return $usuario;
                }
            }
        }catch(PDOException $e){
            echo "Se ha producido un error " . $e->getMessage();
            throw $e;
        } 
    }
    public static function buscarUsuario($telefono){
        try{
            $db = Db::getConnect();
            $consulta = $db->prepare("SELECT * FROM tbl_usuarios where telefono=:telefono");
            $consulta->bindValue(':telefono',$telefono);
            $consulta->execute();
            $respuesta = $consulta->fetch();
            if($respuesta){
                $usuario = new Usuario($respuesta['telefono'],$respuesta['nombre']);
                $usuario->setId($respuesta['id']);
                return $usuario;
            }
        }catch(PDOException $e){
            echo "Se ha producido un error " . $e->getMessage();
            throw $e;
        } 
    }

    public static function getPersonas($id){
        $personas=[];
        $db = Db::getConnect();
        $consulta = $db->prepare("CALL sp_getPersonas(:id)");
        $consulta->bindValue(':id',$id);
        $consulta->execute();
        foreach($consulta->fetchAll() as $persona){
            $personas[]=$persona;
        }
        return $personas;
    }
}
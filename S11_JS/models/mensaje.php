<?php
class Mensaje{
    private $id;
    private $idEmisor;
    private $idReceptor;
    private $texto;
    private $tiempo;
    private $estado;

    function __construct($idEmisor, $idReceptor, $texto)
    {
        $this->idEmisor = $idEmisor;
        $this->idReceptor = $idReceptor;
        $this->texto = $texto;
    }

    /**
     * Get the value of id
     */ 
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set the value of id
     *
     * @return  self
     */ 
    public function setId($id)
    {
        $this->id = $id;

        return $this;
    }

    /**
     * Get the value of idEmisor
     */ 
    public function getIdEmisor()
    {
        return $this->idEmisor;
    }

    /**
     * Set the value of idEmisor
     *
     * @return  self
     */ 
    public function setIdEmisor($idEmisor)
    {
        $this->idEmisor = $idEmisor;

        return $this;
    }

    /**
     * Get the value of idReceptor
     */ 
    public function getIdReceptor()
    {
        return $this->idReceptor;
    }

    /**
     * Set the value of idReceptor
     *
     * @return  self
     */ 
    public function setIdReceptor($idReceptor)
    {
        $this->idReceptor = $idReceptor;

        return $this;
    }

    /**
     * Get the value of texto
     */ 
    public function getTexto()
    {
        return $this->texto;
    }

    /**
     * Set the value of texto
     *
     * @return  self
     */ 
    public function setTexto($texto)
    {
        $this->texto = $texto;

        return $this;
    }

    /**
     * Get the value of tiempo
     */ 
    public function getTiempo()
    {
        return $this->tiempo;
    }

    /**
     * Set the value of tiempo
     *
     * @return  self
     */ 
    public function setTiempo($tiempo)
    {
        $this->tiempo = $tiempo;

        return $this;
    }

    /**
     * Get the value of estado
     */ 
    public function getEstado()
    {
        return $this->estado;
    }

    /**
     * Set the value of estado
     *
     * @return  self
     */ 
    public function setEstado($estado)
    {
        $this->estado = $estado;

        return $this;
    }
    public static function insertar($mensaje){
        try{
            $db = Db::getConnect();
            $db->beginTransaction();
            $consulta = $db->prepare("INSERT INTO tbl_mensajes (idEmisor,idReceptor,texto)".
                " values (:idEmisor,:idReceptor,:text)");
            $consulta->bindValue(':idEmisor',$mensaje->getIdEmisor());
            $consulta->bindValue(':idReceptor',$mensaje->getIdReceptor());
            $consulta->bindValue(':text',$mensaje->getTexto());
            $consulta->execute();
            $db->commit();
        }catch(PDOException $e){
            $db->rollBack();
            echo "Se ha producido un error " . $e->getMessage();
            throw $e;
        }
    }
    public static function getMensajes($id,$id2){
        $mensajes=[];
        $db = Db::getConnect();
        $consulta = $db->prepare("CALL sp_getMensajes(:id,:id2)");
        $consulta->bindValue(':id',$id);
        $consulta->bindValue(':id2',$id2);
        $consulta->execute();
        foreach($consulta->fetchAll() as $mensaje){
            $mensajes[]=$mensaje;
        }
        return $mensajes;
    }
}

?>
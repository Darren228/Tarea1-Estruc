<?php foreach($mensajes as $mensaje):
    $clase = $mensaje['idEmisor']==$_SESSION['id']?'right-bubble':'left-bubble';
?>
<div class="<?=$clase?>">
    <?=$mensaje['texto']?>
    <span class="msg-date"><?=$mensaje['tiempo']?></span>
</div>
<?php endforeach?>
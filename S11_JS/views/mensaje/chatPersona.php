<div class="card">
    <div class="card-header"><?=$receptor->getNombre()?></div>
    <div class="card-body">
        <div id="bloqueMensajes">
            <div id="mensajes" class="chat-message">
                <?php require './views/mensaje/mensajes.php';?>
            </div>
        </div>
        <div class="enviar">
            <form id="frm_enviarMensaje">
                <input type="hidden" name="action" value="enviarMensajeChat">
                <input type="hidden" name="telefono" value="<?=$receptor->getTelefono()?>">
                <div class="form-group">
                    <label for="texto" class="form-label mt-4">Texto</label>
                    <textarea name="texto" id="texto" rows="2" 
                        class="form-control"   required></textarea>
                </div>
                <button class="btn btn-outline-primary float-right" type="submit">Enviar</button>
            </form>
        </div>
    </div>
</div>
<script src="./views/js/app.js"></script>
<div class="card">
    <div class="card-header">
        Enviar mensaje
    </div>
    <div class="card-body">
        <form id="frm_nuevoMensaje">
            <input type="hidden" name="action" value="enviarMensaje">
            <div class="form-group">
                <label for="idReceptor" class="form-label mt-4">Telefono:</label>
                <input type="tel" class="form-control" name="idReceptor" id="idReceptor"
                    pattern="[0-9]{4}-[0-9]{4}" required>
                <div id="nombreReceptor"></div>
            </div>
            <div select name= "buscar usuario"</div>
            <div class="form-group">
                <label for="texto" class="form-label mt-4">Texto:</label>
                <textarea class="form-control" name="texto" rows="3"
                required></textarea>
            </div>
            <button id="btnEnviarMensaje" type="submit" class="btn btn-outline-primary float-right">Enviar</button>
        </form>
    </div>
    <div class="card-footer">
        <button class="btn btn-outline-secondary">Volver</button>
    </div>
</div>
<script src="./views/js/nuevoMensaje.js"></script>
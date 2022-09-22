
    <div class="container">
        <div class="card col-sm-6 mx-auto mt-5">
            <div class="card-header">Registro de usuario</div>
            <div class="card-body">
                <h4 class="card-title">Digite los datos requeridos</h4>
                <form id="frm_registro">
                    <input type="hidden" name="action" value="iUsuario">
                    <div class="form-group">
                        <label for="nombre" class="form-label mt-4">Nombre</label>
                        <input type="tel" class="form-control" id="nombre" name="nombre" 
                            required>
                    </div>
                    <div class="form-group">
                        <label for="telefono" class="form-label mt-4">Telefono registrado</label>
                        <input type="tel" class="form-control" id="telefono" name="telefono" 
                            placeholder="####-####" pattern="[0-9]{4}-[0-9]{4}" required>
                    </div>
                    <div class="form-group">
                        <label for="clave" class="form-label mt-4">Clave: </label>
                        <input type="password" class="form-control" id="clave" name="clave"
                            placeholder="clave" required>
                    </div>
                    <button class="btn btn-primary btn-lg float-right" type="submit">Iniciar sesion</button>
                </form>
                <br><br><br>
                <p class="float-right">Si posee cuenta, <a id="btnLogin">inicie sesion!</a></p>
            </div>
            <div class="card-footer">
                2022
            </div>
        </div>
    </div>
    <script src="./views/js/app.js"></script>

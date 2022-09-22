
    <div class="container">
        <div class="card col-sm-6 mx-auto mt-5">
            <div class="card-header">Inicio de sesion</div>
            <div class="card-body">
                <h4 class="card-title">Digite los datos requeridos</h4>
                <form id="frm_login">
                    <input type="hidden" name="action" value="iniciarSesion">
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
                <p class="float-right">Si no posee cuenta, <a id="btnRegistro">registrese!</a></p>
            </div>
            <div class="card-footer">
                2022
            </div>
        </div>
    </div>
    <script src="./views/js/app.js"></script>
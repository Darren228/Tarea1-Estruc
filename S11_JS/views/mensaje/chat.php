<nav class="navbar navbar-expand-md bg-dark navbar-dark">
  <a class="navbar-brand" href="#">SCI</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="" id="btnSalir">Salir</a>
      </li>   
    </ul>
  </div>  
</nav>
<div class="container-fluid">
    <div class="row">
        <div class="card col-sm-4 float-left">
            <div class="card-header">
                PERSONAS
                <button class="btn btn-primary float-right" id="btnNuevo">
                        +  
                </button>
            </div>
            <div class="card-body">
                <div id="bloquePersonas">
                    <?php foreach($personas as $persona):?>
                        <button class="btn btn-outline-primary btn-block"
                            id="<?=$persona['telefono']?>"
                            onClick="cargarChat(this)"
                            >
                            <?=$persona['nombre']?>
                        </button>
                    <?php endforeach;?>
                </div>
            </div>
        </div>
        <div class="container col-sm-8 float-right" id="chatPersona">
        </div>
    </div>
</div>
<script src="./views/js/app.js"></script>
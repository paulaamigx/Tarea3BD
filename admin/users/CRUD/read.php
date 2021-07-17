<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>


<?php
/* Este archivo debe manejar la lógica de obtener los datos de un determinado usuario */
	$url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	$url_components = parse_url($url);
	  
	parse_str($url_components['query'], $params);
	      
	$userId = $params['id'];

	$query = "SELECT  nombre, apellido, correo, pais, fecha_registro FROM usuario WHERE id=".$userId;
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
		echo $query;
	}

	$arr= pg_fetch_array($res, 0, PGSQL_NUM);

	$query = "SELECT  nombre FROM pais WHERE cod_pais=".$arr[3];
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
		echo $query;
	}
	
	$country = pg_fetch_array($res, 0, PGSQL_NUM)[0];
	$userHTML = "<p>Id: ".$userId."</p>".
							"<p>Nombre: ".$arr[0]."</p>".
							"<p>Apellido: ".$arr[1]."</p>".
							"<p>Correo: ".$arr[2]."</p>".
							"<p>País : ".$country."</p>".
							"<p>Fecha de Ingreso : ".explode(" ",$arr[4])[0]."</p>".

              "<div class='d-flex justify-content-end'>
                  <a href='/admin/users/all.html' class='btn btn-secondary'>Volver</a>
                  <!-- Estos links deberían tener el ID asociado -->
                  <a href='/admin/users/update.html?id=".$userId."' class='btn btn-warning mx-3'>Editar <i class='fas fa-edit'></i></a>
                  <a href='/admin/users/CRUD/delete.php?id=".$userId."' class='btn btn-danger'>Borrar <i class='fas fa-trash-alt'></i></a></td>
              </div>"

?>

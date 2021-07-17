<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica para crear un usuario como admin */
	//---- id -------
	$query = "SELECT pais, id FROM usuario WHERE id=( SELECT max(id) FROM usuario)";
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
		echo $query;
	}
 	$newId = pg_fetch_array($res, 0, PGSQL_NUM)[1]+1;

	$date =  "'".date("Y/m/d")."'";


  $params =  array($newId,
										"'".$_REQUEST["name"]."'",
										"'".$_REQUEST['surname']."'",
										"'".$_REQUEST['email']."'",
 										"'".substr(password_hash($_REQUEST['password1'], PASSWORD_DEFAULT),3,20)."'",

										"'".$_REQUEST['country']."'",
										$date,
										0);
	$params = implode(",",$params);

	
	$query = "INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro, admin) VALUES (".$params.")";
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
		echo $query;
	}
	
		echo "<h2>Registro exitoso.</h2>";

		echo "<a href='./../../../index.html'> Volver a página principal</a>";

?>

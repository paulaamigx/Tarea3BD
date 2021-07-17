<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica de actualizar los datos de un usuario como admin */

	$query = "UPDATE usuario SET nombre='".$_REQUEST["name"].
														 "',apellido='".$_REQUEST["surname"].
														 "',correo='".$_REQUEST["email"].
														 "',contraseña='".$_REQUEST["password"].
														 "',pais=".$_REQUEST["country"].
						 " WHERE id =".$_REQUEST["id"];
	
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
		echo $query;
		exit;
	}
		echo "<h2>Registro exitoso.</h2>";

		echo "<a href='./../../../index.html'> Volver a página principal</a>";


?>

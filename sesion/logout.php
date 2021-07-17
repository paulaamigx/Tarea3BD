<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica de cerrar una sesión */
	$query = "UPDATE sesion SET is_logged=0";
	$res = pg_query($dbconn, $query);

	if($res){
			header("Location: ./../index.html");
	}
	else{
		echo "Error conexión";
	}

?>

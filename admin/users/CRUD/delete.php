<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica de borrar un usuario (y los registros relacionados) como admin */
	$url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	$url_components = parse_url($url);
	  
	parse_str($url_components['query'], $params);
	      
	$userId = $params['id'];

	$query = "DELETE FROM usuario WHERE id=".$userId; 
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
		echo $query;
	}
		echo "<h2>Eliminación  exitosa.</h2>";

		echo "<a href='./../../../index.html'> Volver a página principal</a>";


?>

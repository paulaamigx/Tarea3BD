<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica para obtener la información del perfil */

	//------get user-------
	$query = "SELECT user_id FROM  sesion WHERE lock='X'";
	$res = pg_query($dbconn, $query);
	if (!$res) {
  	echo "Error en conexion.\n";
  	echo $query;
  	exit;
	}
	$userId = pg_fetch_array($res, 0, PGSQL_NUM)[0];

	//------get evrything from user---------
	$query = "SELECT nombre, apellido, correo, pais, fecha_registro FROM usuario WHERE id=".$userId;
	$res = pg_query($dbconn, $query);
	
	if (!$res) {
  	echo "Error en conexion.\n";
  	echo $query;
  	exit;
	}
	$arr = pg_fetch_array($res, 0, PGSQL_NUM);
	
	//------get country----------
	$query = "SELECT nombre FROM pais WHERE cod_pais=$arr[3]";
	$res = pg_query($dbconn, $query);
	
	if (!$res) {
  	echo "Error en conexion.\n";
  	echo $query;
  	exit;
	}
	$country = pg_fetch_array($res, 0, PGSQL_NUM)[0];
	$fullName 	= $arr[0]." ".$arr[1];
	$email 			= $arr[2];
	
	$regDate		= explode(" ",$arr[4])[0];


?>

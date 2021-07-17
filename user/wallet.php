<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica para obtener la información de la billetera */

	//------get user-------
	$query = "SELECT user_id FROM  sesion WHERE lock='X'";
	$res = pg_query($dbconn, $query);
	if (!$res) {
  	echo "Error en conexion.\n";
  	echo $query;
  	exit;
	}
	$userId = pg_fetch_array($res, 0, PGSQL_NUM)[0];

	//-------- select wallet with query -----

	$query="SELECT t2.sigla_moneda, t2.nombre_moneda, t2.balance, t1.valor, t1.valor*t2.balance
					FROM (	SELECT id_moneda, valor
							FROM precio_moneda s1
							WHERE fecha = (SELECT MAX(fecha) 
										   FROM precio_moneda s2 
										   WHERE s1.id_moneda = s2.id_moneda)
							ORDER BY id_moneda, fecha) t1
					INNER JOIN (
						SELECT moneda.sigla as sigla_moneda, moneda.nombre as nombre_moneda, usuario_tiene_moneda.balance as balance, moneda.id as id_moneda
						FROM moneda
						INNER JOIN usuario_tiene_moneda
						ON moneda.id = usuario_tiene_moneda.id_moneda
						WHERE usuario_tiene_moneda.id_usuario=".$userId.") t2
					ON t2.id_moneda = t1.id_moneda";
	$res = pg_query($dbconn, $query);	
	if (!$res) {
  	echo "Error en conexion.\n";
  	echo $query;
  	exit;
	}
	$arr = pg_fetch_all($res);

	//------ prepare variable for html output -------
	$tableHTML = "";
	foreach($arr as $row){
		$tableHTML .= "<tr>";
		foreach($row as $field){
			$tableHTML .= "<td>".$field."</td>";
		}
		$tableHTML .= "</tr>";
	}

?>

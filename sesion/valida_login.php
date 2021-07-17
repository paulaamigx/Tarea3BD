<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php 
/* Este archivo debe manejar la lógica de iniciar sesión */

	$query = "SELECT contraseña, admin, id FROM usuario WHERE correo='";
	$query.=$_POST["email"];
	$query.= "'";
	$res = pg_query($dbconn, $query);
	
	if (!$res) {
  	echo "Error en conexion.\n";
  	exit;
	}

	$arr = pg_fetch_array($res, 0, PGSQL_NUM);
	if($arr[0] == $_POST["password"]){
   	$result = pg_prepare($dbconn, "myQuery", "UPDATE sesion SET is_logged =1, is_admin = $1, user_id = $2 WHERE lock='X'");
		$result = pg_execute($dbconn, "myQuery", array($arr[1],$arr[2]));
	  if ($result) {
			header("Location: ./../index.html");
 		 } else {
     	echo "User must have sent wrong inputs\n";
  }

	}
	else{
		echo "Datos Incorrectos <br>";
		echo "<button onclick='history.go(-1);'>Volver </button>";
	}


?>

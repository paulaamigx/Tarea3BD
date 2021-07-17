<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe validar los datos de registro y manejar la lógica de crear un usuario desde el formulario de registro */
	
	
	if($_POST["password1"] == $_POST["password2"]){
		$query = "SELECT MAX(id) FROM usuario";
		$res = pg_query($dbconn, $query);
		
		if (!$res) {
  		echo "Error en conexion.\n";
			echo $query;
  		exit;
		}
		$userId = pg_fetch_array($res, 0, PGSQL_NUM)[0]+1;
		$date =  "'".date("Y/m/d")."'";
  	$params =  array($userId,
											"'".$_POST['name']."'",
											"'".$_POST['surname']."'",
											"'".$_POST['email']."'",
  										"'".substr(password_hash($_REQUEST['password1'], PASSWORD_DEFAULT),3,20)."'",

											$_POST['country'],
											$date,
											0);

		$params = implode(",",$params);
		$query = "INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro,admin) VALUES(".$params.")";
		$res = pg_query($dbconn, $query);
		
		if (!$res) {
  		echo "Error en conexion.\n";
			echo $query;
  		exit;
		}
		
		echo "<h2>Registro exitoso. Vuelve a la página pricipal para iniciar sesión</h2>";
		echo "<a href='./../index.html'> Página Principal </a>";

	}
	else{
		echo "<h2>Contraseñas deben coincidir.</h2>";
		echo "<button onclick='history.go(-1);'>Volver </button>";

	}
					
?>


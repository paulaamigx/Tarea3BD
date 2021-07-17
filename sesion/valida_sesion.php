<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe usarse para comprobar si existe una sesión válida 
   Considerar qué pasa cuando la sesión es válida/inválida para cada página:
   - Página principal
   - Mi perfil
   - Mi billetera
   - Administración de usuarios y todo el CRUD
   - Iniciar Sesión
   - Registrarse
*/

	/* Se trabaja con flags que determinan que pestañas son visibles y que paginas estan habilitadas segun si hay alguien logueade y si esa persona es admin o no. 
	En cada archivo html no accesible en alguno de estos casos, se revisa si se esta habilitade y si no se redirecciona al index
	Para la visibilidad de las pestañas, se le asigna de inmediato el atributo css que corresponde*/
	$query = "SELECT is_logged, is_admin, user_id FROM sesion";
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
	}
	$arr = pg_fetch_array($res, 0, PGSQL_NUM);

	if($arr[0] ){ //is logged 
		$logOutVisibility	 = "visibility: visible";
		$logInVisibility	 = "visibility: hidden";
		$signUpVisibility	 = "visibility: hidden";

		$logInEnabled	 	= false;
		$signUpEnabled	= false;	

		if($arr[1]){ //is admin
			$profileVisibility = "visibility: visible";
			$walletVisibility	 = "visibility: hidden";
			$usersVisibility	 = "visibility: visible";

			$profileEnabled	= true;
			$walletEnabled 	= false;
			$usersEnabled  	= true;
		}
			
		else{// is user
			$profileVisibility = "visibility: visible";
			$walletVisibility	 = "visibility: visible";
			$usersVisibility	 = "visibility: hidden";

			$profileEnabled	= true;
			$walletEnabled  = true;
			$usersEnabled 	= false;
		}
	}

	else{ //is not logged 
		$logOutVisibility	 = "visibility: hidden";
		$logInVisibility	 = "visibility: visible";
		$signUpVisibility	 = "visibility: visible";
		$profileVisibility = "visibility: hidden";
		$walletVisibility	 = "visibility: hidden ";
		$usersVisibility	 = "visibility: hidden";

		$profileEnabled = false;
		$walletEnabled 	= false;
		$usersEnabled  	= false;
		$logInEnabled	 	= true;
		$signUpEnabled	= true;	
	}

?>

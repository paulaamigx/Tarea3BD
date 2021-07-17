<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
/* Este archivo debe manejar la lógica de obtener los datos de todos los usuarios */
	$query = "SELECT id, nombre, apellido, correo FROM usuario";
	$res = pg_query($dbconn, $query);

	if(!$res){
		echo "Error conexión";
	}

	$arr = pg_fetch_all($res);
	
	$usersHTML = "";
	foreach($arr as $row){
		$usersHTML .= "<tr>";
		$userId = $row['id'];
		foreach($row as $field){
			$usersHTML .= "<td>".$field."</td>";
		}
    $usersHTML .= "<td><a href='/admin/users/read.html?id=".$userId."' class='btn btn-primary'>Ver <i
                class='fas fa-search'></i></a>
        <a href='/admin/users/update.html?id=".$userId."' class='btn btn-warning'>Editar <i
                class='fas fa-edit'></i></a>
        <a href='/admin/users/CRUD/delete.php?id=".$userId."' class='btn btn-danger'>Borrar <i
                class='fas fa-trash-alt'></i></a>
    </td>";
		$usersHTML .= "</tr>";
	}

?>

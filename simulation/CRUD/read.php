<?php include 'vars.php' ?>
<?php include 'tableVars.php'?>
<?php
	$url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	$url_components = parse_url($url);
	  
	parse_str($url_components['query'], $params);
	      
	$id = $params['id'];
	$tableName= $params['tableName'];

	######  GET	#######

	$ch = curl_init();
	$url = 'http://127.0.0.1:5000/api/'.$tableName.'/'.$id;
	$url = str_replace(' ', '_', $url);
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

	curl_setopt($ch, CURLOPT_HTTPGET);
	$content = curl_exec($ch);
	curl_close($ch);
	$item = json_decode($content, true)[$tableName];
	$itemHTML = "";
	foreach($fields[$tableName] as $index=>$field){
		$itemHTML .= "<p>".$fieldsNames[$tableName][$index].": ".$item[$field]."</p>";
	}

	$itemHTML .=
              "<div class='d-flex justify-content-end'>
                  <a href='/simulation/CRUD/all.html?tableName=".$tableName."' class='btn btn-secondary'>Volver</a>
                  <a href='/simulation/CRUD/update.html?id=".$id."&tableName=".$tableName."' class='btn btn-warning mx-3'>Editar <i class='fas fa-edit'></i></a>
                  <a href='/simulation/CRUD/delete.php?id=".$id."&tableName=".$tableName."' class='btn btn-danger'>Borrar <i class='fas fa-trash-alt'></i></a></td>
              </div>"
?>

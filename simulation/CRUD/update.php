<?php include './../../include/navbar.html'; ?>
<?php include 'vars.php'; ?>
<?php
	$url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	$url_components = parse_url($url);
	parse_str($url_components['query'], $params);
	$id = $params['id'];
	$tableName= $params['tableName'];
	echo $tableName;

	$ch = curl_init();
	$url = 'http://127.0.0.1:5000/api/'.$tableName."/".$_REQUEST["id"];
	echo $url;
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_HEADER, false);

	$data = array();
	foreach($fields[$tableName] as $key=>$field){
		echo $field;
		$arr = array($field => $_REQUEST[$field]);
		$data += $arr;
	}
	
	$data = json_encode($data);
	echo $data;
	/*
	$data = array(
					"username"	=> $_REQUEST["name"],
					"surname"		=> $_REQUEST["surname"],
					"email"			=> $_REQUEST["email"],
					"password"	=> $_REQUEST["password"],
					"country"		=> $_REQUEST["country"],	
			 		);
	$data = json_encode($data);
	*/
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
	curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
	
	$content = curl_exec($ch);

	curl_close($ch);

	echo "<h2>Actualización completada</h2>";
	echo "<a href='./../../index.html'> Volver a página principal</a>";


?>

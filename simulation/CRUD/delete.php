<?php include './../../include/navbar.html'; ?>

<?php
	$url = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
	$url_components = parse_url($url);
	  
	parse_str($url_components['query'], $params);
	      
	$id = $params['id'];
	$tableName= $params['tableName'];

	$ch = curl_init();
	$url = 'http://127.0.0.1:5000/api/'.$tableName.'/'.$id;
	echo $url;
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

	$content = curl_exec($ch);
	curl_close($ch);
	header("Location: ./all.html?tableName=".$tableName)


?>


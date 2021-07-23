<?php include './../../include/navbar.html'; ?>
<?php include 'vars.php' ?>
<?php
	$tableName = $_REQUEST["tableName"];
	$ch = curl_init();
	$url = "http://127.0.0.1:5000/api/".$tableName."/";
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	echo $tableName;
	$data = array();
	foreach($fields[$tableName] as $key=>$field){
		$arr = array($field => $_REQUEST[$field]);
		$data += $arr;
	}
	
	$data = json_encode($data);
	echo $data;
	curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
	$content = curl_exec($ch);

	curl_close($ch);
	echo "<h2>Creación exitosa.</h2>";
	echo "<a href='./../../index.html'> Volver a página principal</a>";

?>

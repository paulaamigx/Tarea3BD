<?php include '../../include/navbar.html'; ?>

<?php
	echo "as";
	$queryId = $_REQUEST["queryId"];
	$param= $_REQUEST["param"];
	$ch = curl_init();
	$url = "http://127.0.0.1:5000/api/consultas/".$queryId."/".$param;
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$content = curl_exec($ch);
	$content = json_decode($content, true);


	curl_close($ch);
	$htmlTable = '
        <div class="row p-3">
            <div class="col">
                <div class="container shadow-lg rounded m-auto p-5">';
	$htmlTable .= "<table class='table'>	<tr>";

	foreach($content as $key){
		foreach($key as $field ){
			foreach($field as $key=>$value){
				$htmlTable .= "<th>".$key."</th>";
			}
			$htmlTable .= "</tr>";
			$htmlTable .= "<tr>";
			foreach($field as $key=>$value){
				$htmlTable .= "<td>".$value."</td>";
			}
			$htmlTable .= "<tr>";
		}
	}

	$htmlTable .= "</table></div></div></div>";
	echo $htmlTable;
	

?>

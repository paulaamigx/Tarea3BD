<?php

	$tablesFieldsNames =  array(
										"users" 					=> 	array("ID", "Nombre", "Apellido", "Correo"),
										"countries"				=> 	array("Código Pais", "Pais"),
										"accounts"				=> 	array("ID", "Código Usuarix", "Balance"),
										"userCurrencies"	=>	array("Código Usuarix", "Código Moneda", "Balance"),
										"currencyValues"	=>	array("Código Moneda", "Valor", "Fecha"),
										"currencies"				=> 	array("Sigla", "Nombre")
	
									);
	$tablesFields =  array(
										"users" 					=> 	array("id", "nombre","apellido","correo"),
										"countries"				=> 	array("id", "nombre"),
										"accounts"				=> 	array("id", "id_usuario", "balance"),
										"userCurrencies"	=>	array("id_usuario", "id_moneda", "balance"),
										"currencyValues"	=>	array("id_moneda",  "valor", "fecha"),
										"currencies"				=>	array("sigla", "nombre")

									);
	$tableTitle = array(
									"users" 					=> "Usuarixs",
									"countries"				=> "Paises",
									"accounts"				=> "Cuenta Bancaria",
									"userCurrencies"	=> "Usuarix/Moneda",
									"currencyValues"	=> "Precio Moneda",
									"currencies"			=> "Moneda"
								);

?>

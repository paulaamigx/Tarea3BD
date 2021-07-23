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
										"users" 					=> 	array("id", "username","surname","email"),
										"countries"				=> 	array("id", "countryName"),
										"accounts"				=> 	array("id", "userId", "balance"),
										"userCurrencies"	=>	array("userId", "currencyId", "balance"),
										"currencyValues"	=>	array("currencyId",  "value", "createdAt"),
										"currencies"				=>	array("sigla", "name")

									);
	$tableTitle = array(
									"users" 					=> "Usuarixs",
									"countries"				=> "Paises",
									"accounts"				=> "Cuenta Bancaria",
									"userCurrencies"	=> "Usuarix/Moneda",
									"currencyValues"	=> "Precio Moneda",
									"currencies"				=> "Moneda"
								);

?>

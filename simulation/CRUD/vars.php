<?php
	$fields = array(
									"users"						=> 	array( "username", "surname", "email",
																				 			"password", "countryId", "id", "createdAt"),
									"countries" 			=> 	array("countryName", "id"),
									"accounts"				=>	array("id", "userId", "balance"),
									"userCurrencies"	=>	array("currencyId", "userId", "balance"),
									"currencyValues"	=>	array("currencyId",  "value", "createdAt"),
									"currencies"				=>  array("id", "sigla", "name")
						);
	$fieldsNames = array(
									"users"						=> 	array("Nombre", "Apellido", "Correo Elecrtónico", 
																							"Contraseña", "Pais", "ID", "Fecha de creación"),
									"countries" 			=> 	array("Nombre Pais", "Código País"),	
									"accounts"				=>	array("ID", "Código Usarix", "Balance"),
									"userCurrencies"	=>	array("Código Usuarix", "Código Moneda", "Balance"),
									"currencyValues"	=>	array("Código Moneda", "Valor", "Fecha"),
									"currencies"				=>  array("ID", "Sigla", "Nombre")

						);
	#default: text
	$fieldType = array(
									"email"				=>	"email",
									"password"		=>	"password",
									"balance"			=>  "number",
									"userId"			=>  "number",
									"currencyId"	=>  "number",
									"value"				=> 	"number"
						);

?>

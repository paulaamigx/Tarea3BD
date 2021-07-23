<?php
	$fields = array(
									"users"						=> 	array( "nombre", "apellido", "correo",
																				 			"contrasena", "pais", "id", "fecha_registro"),
									"countries" 			=> 	array("nombre", "id"),
									"accounts"				=>	array("id", "id_usuario", "balance"),
									"userCurrencies"	=>	array("id_usuario", "id_moneda", "balance"),
									"currencyValues"	=>	array("id_moneda",  "valor", "fecha"),
									"currencies"				=>  array("id", "sigla", "nombre")
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
									"correo"			=>	"email",
									"contrasena"	=>	"password",
									"balance"			=>  "number",
									"id_usuario"	=>  "number",
									"id_moneda	"	=>  "number",
									"valor"				=> 	"number"
						);

?>

<?php

require("database.php");
$arr = array();
header("Content-type: application/json");

if (isset($_GET["gav"]))
{
	try
	{
		$str_json = $_GET["gav"];
		$json = json_decode($str_json, true);
		
		$db = Database::getInstance();
		$query = "INSERT INTO `currencies_gav` SET currency = ?, date = ?, CAD = ?, HKD = ?, ISK = ?, PHP = ?, DKK = ?, HUF = ?, CZK = ?, GBP = ?, RON = ?, SEK = ?, INR = ?, BRL = ?, RUB = ?, HRK = ?, JPY = ?, THB = ?, CHF = ?, EUR = ?, MYR = ?, BGN = ?, TRY = ?, CNY = ?, NOK = ?, NZD = ?, ZAR = ?, USD = ?, MXN = ?, SGD = ?, AUD = ?, ILS = ?, KRW = ?, PLN = ?";
		
		$curr = $json["TargetCurrencies"];
		$db->exec($query, [$json["Currency"], $json["Date"], $curr["CAD"], $curr["HKD"], $curr["ISK"], $curr["PHP"], $curr["DKK"], $curr["HUF"], $curr["CZK"], $curr["GBP"], $curr["RON"], $curr["SEK"], $curr["INR"], $curr["BRL"], $curr["RUB"], $curr["HRK"], $curr["JPY"], $curr["THB"], $curr["CHF"], $curr["EUR"], $curr["MYR"], $curr["BGN"], $curr["TRY"], $curr["CNY"], $curr["NOK"], $curr["NZD"], $curr["ZAR"], $curr["USD"], $curr["MXN"], $curr["SGD"], $curr["AUD"], $curr["ILS"], $curr["KRW"], $curr["PLN"]]);
		
		$arr["code"] = "1";
		$arr["message"] = "success";
		echo json_encode($arr);
	}
	catch(Exception $ex)
	{
		$arr["code"] = "-1";
		$arr["message"] = $ex->getMessage();
		echo json_encode($arr);
	}
}
else if (isset($_GET["lav"]))
{
	try
	{
		$str_json = $_GET["lav"];
		$json = json_decode($str_json, true);
		
		$db = Database::getInstance();
		$query = "INSERT INTO `currencies_lav` SET currency1 = ?, date1 = ?, CAD1 = ?, HKD1 = ?, ISK1 = ?, PHP1 = ?, DKK1 = ?, HUF1 = ?, CZK1 = ?, GBP1 = ?, RON1 = ?, SEK1 = ?, INR1 = ?, BRL1 = ?, RUB1 = ?, HRK1 = ?, JPY1 = ?, THB1 = ?, CHF1 = ?, EUR1 = ?, MYR1 = ?, BGN1 = ?, TRY1 = ?, CNY1 = ?, NOK1 = ?, NZD1 = ?, ZAR1 = ?, USD1 = ?, MXN1 = ?, SGD1 = ?, AUD1 = ?, ILS1 = ?, KRW1 = ?, PLN1 = ?, currency2 = ?, date2 = ?, CAD2 = ?, HKD2 = ?, ISK2 = ?, PHP2 = ?, DKK2 = ?, HUF2 = ?, CZK2 = ?, GBP2 = ?, RON2 = ?, SEK2 = ?, INR2 = ?, BRL2 = ?, RUB2 = ?, HRK2 = ?, JPY2 = ?, THB2 = ?, CHF2 = ?, EUR2 = ?, MYR2 = ?, BGN2 = ?, TRY2 = ?, CNY2 = ?, NOK2 = ?, NZD2 = ?, ZAR2 = ?, USD2 = ?, MXN2 = ?, SGD2 = ?, AUD2 = ?, ILS2 = ?, KRW2 = ?, PLN2 = ?";
		
		$curr = $json["API"]["rates"];
		$curr2 = $json["APIV4"]["rates"];
		$db->exec($query, [$json["API"]["base"], $json["API"]["date"], $curr["CAD"], $curr["HKD"], $curr["ISK"], $curr["PHP"], $curr["DKK"], $curr["HUF"], $curr["CZK"], $curr["GBP"], $curr["RON"], $curr["SEK"], $curr["INR"], $curr["BRL"], $curr["RUB"], $curr["HRK"], $curr["JPY"], $curr["THB"], $curr["CHF"], $curr["EUR"], $curr["MYR"], $curr["BGN"], $curr["TRY"], $curr["CNY"], $curr["NOK"], $curr["NZD"], $curr["ZAR"], $curr["USD"], $curr["MXN"], $curr["SGD"], $curr["AUD"], $curr["ILS"], $curr["KRW"], $curr["PLN"], $json["APIV4"]["base"], $json["APIV4"]["date"], $curr2["CAD"], $curr2["HKD"], $curr2["ISK"], $curr2["PHP"], $curr2["DKK"], $curr2["HUF"], $curr2["CZK"], $curr2["GBP"], $curr2["RON"], $curr2["SEK"], $curr2["INR"], $curr2["BRL"], $curr2["RUB"], $curr2["HRK"], $curr2["JPY"], $curr2["THB"], $curr2["CHF"], $curr2["EUR"], $curr2["MYR"], $curr2["BGN"], $curr2["TRY"], $curr2["CNY"], $curr2["NOK"], $curr2["NZD"], $curr2["ZAR"], $curr2["USD"], $curr2["MXN"], $curr2["SGD"], $curr2["AUD"], $curr2["ILS"], $curr2["KRW"], $curr2["PLN"]]);
		
		$arr["code"] = "1";
		$arr["message"] = "success";
		echo json_encode($arr);
	}
	catch(Exception $ex)
	{
		$arr["code"] = "-1";
		$arr["message"] = $ex->getMessage();
		echo json_encode($arr);
	}
}
else
{
	$arr["code"] = "0";
	$arr["message"] = "no parameter";
	echo json_encode($arr);
}
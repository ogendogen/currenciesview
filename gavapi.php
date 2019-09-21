<?php

require("database.php");
$ret = array();
header("Content-type: application/json");

try
{
    $base = $_GET["base"];
    $target = $_GET["target"];

    if (!isset($base) || !isset($target))
    {
        throw new Exception("Missing parameters");
    }

    if (strlen($base) != 3 || strlen($target) != 3)
    {
        throw new Exception("Incorrect parameters value");
    }

    $db = Database::getInstance();
    
    $result = $db->exec("SELECT ".$target.", date FROM `currencies_gav` WHERE currency = ? ORDER BY date ASC", [$base]);
    $ret["date"] = array();
    $ret[$target] = array();
    foreach ($result as $row)
    {
        array_push($ret[$target], $row[$target]);
        array_push($ret["date"], $row["date"]);
    }

    echo json_encode($ret);
}
catch(Exception $e)
{
    $ret = array();
    $ret["error"] = true;
    $ret["message"] = $e->getMessage();
    echo json_encode($ret);
}
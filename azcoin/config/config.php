<?php
$dbHost = 'localhost';
$dbName = 'AZMerit';
$dbUser = 'postgres';
$dbPass = '1234';

try{
    $conexao = new PDO("pgsql:host=$dbHost;dbname=" . $dbName, $dbUser, $dbPass);
    //echo "conexao relizada com sucesso";
}catch(PDOException $err){
    //echo "banco não conectado" . " " .$err->getMessage();
}

?>
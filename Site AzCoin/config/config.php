<?php
$dbHost = 'localhost';
$dbName = 'AZMerit';
$dbUser = 'postgres';
$dbPass = '1234';

try{
    $conexao = new PDO("pgsql:host=$dbHost;dbname=" . $dbName, $dbUser, $dbPass);
    //echo "conexao relizada com sucesso";
    echo '<span style="color:#AFA;text-align:center;">Request has been sent. Please wait for my reply!</span>';
}catch(PDOException $err){
    //echo "banco não conectado" . " " .$err->getMessage();
}

?>
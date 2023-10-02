<?php
$hostname = "localhost";
$username = "postgres";
$password = '1234';
$db= "azcrud";

$conn = pg_connect("host=$hostname dbname=$db user=$username password=$password");

if(!$conn){
    echo '<h1>errou</h1>';
}
else{
    echo "<h1>Funfou</h1>";
}
?>
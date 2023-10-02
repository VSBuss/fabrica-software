<?php
$hostname = "localhost";
$username = "root";
$password = "";
$db= "azcrud";
$conn = new mysqli($hostname,$username,$password,$db);
if(!$conn){
    echo '<h1>errou</h1>';
}
else{
    echo "<h1>Funfou</h1>";
}
?>
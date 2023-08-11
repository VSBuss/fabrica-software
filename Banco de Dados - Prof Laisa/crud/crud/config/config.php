<?php
$dbHost = 'localhost';
$dbName = 'crud_db';
$dbUser = 'postgres';
$dbPass = '123';

$dsn = "pgsql:host=$dbHost;dbname=$dbName;";
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];

try {
    $pdo = new PDO($dsn, $dbUser, $dbPass, $options);
} catch (PDOException $e) {
    die($e->getMessage());
}

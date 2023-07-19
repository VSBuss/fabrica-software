<?php
// buscarDados.php
$servername = "localhost";
$username = "username";
$password = "";
$dbname = "myDB";

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname);
// Checar conexão
if ($conn->connect_error) {
  die("Conexão falhou: " . $conn->connect_error);
}

$sql = "SELECT nome, sobrenome, email FROM minhaTabela";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // Saída dos dados de cada linha
  while($row = $result->fetch_assoc()) {
    $data[] = $row;
  }
  echo json_encode($data);
} else {
  echo "0 resultados";
}
$conn->close();
?>

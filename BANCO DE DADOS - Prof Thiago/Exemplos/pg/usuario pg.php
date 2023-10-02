<?php
    include 'connect_pg.php';

    if(isset($_POST['cadastrar'])){
        $nome = $_POST['nome'];
        $email = $_POST['email'];
        $senha = $_POST['senha'];

        $sql = "INSERT INTO usuario (nome,email,senha) VALUES ('$nome','$email','$senha');";

        $result = pg_query($conn,$sql);

        if($result){
            echo "<h1>CADASTRADO NO SUL DO CESSO</h1>";

    }}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ususario</title>
</head>
<body>
    <form method="post">
        <input type="text" placeholder="Digite seu nome" name="nome">
        <br>
        <input type="text" placeholder="Digite seu email" name="email">
        <br>
        <input type="password" placeholder="Digite sua Senha" name="senha">
        <br>
        <input type="submit" value="Cadastrar" id="cadastrar" name="cadastrar">
        <br>
    </form>
</body>
</html>
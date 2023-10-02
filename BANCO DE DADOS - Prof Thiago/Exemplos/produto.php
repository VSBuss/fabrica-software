<?php
    include 'connect.php';

    if(isset($_POST['cadastrar'])){
        $nome = $_POST['nome'];
        $desc = $_POST['desc'];
        $preco = $_POST['preço'];
        $qtde = $_POST['qtde'];

        $sql = "INSERT INTO produto (nome,descricao,preco,qtde) VALUES ('$nome','$desc','$preco','$qtde');";

        $result = mysqli_query($conn,$sql);

        if($result){
            echo "<h1>CADASTRADO NO SUL DO CESSO</h1>";
        }else{
            die(mysqli_error($conn));
        }
    }



?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>produto</title>
</head>
<body>
    <form method="POST">
        <input type="text" placeholder="Digite o nome do Produto" name="nome">
        <br>
        <input type="text" placeholder="Digite sua Descrição" name="desc">
        <br>
        <input type="text" placeholder="Digite seu Preço" name="preço">
        <br>
        <input type="text" placeholder="Digite sua Quantidade" name="qtde">
        <br>
        <input type="submit" value="Cadastrar" id="cadastrar" name="cadastrar">
        <br>
    </form>
</body>
</html>
<?php
    session_start();
    include_once("conexao.php");

    $nome = filter_input(INPUT_POST, 'nome_cad');
    $cpf = filter_input(INPUT_POST, 'cpf');
    $data_nasc = filter_input(INPUT_POST, 'data_nasc');
    $sexo = filter_input(INPUT_POST, 'sexo');
    $telefone = filter_input(INPUT_POST, 'fone');
    $endereco = filter_input(INPUT_POST, 'endereco');
    $email = filter_input(INPUT_POST, 'email_cad');
    $senha = filter_input(INPUT_POST, 'senha_cad');     

    $result_usuario = "INSERT INTO pessoa (nome, cpf, data_nasc, sexo, telefone, 
    endereco, email, senha) VALUES ('$nome', '$cpf', '$data_nasc', '$sexo', '$telefone', '$endereco', 
    '$email', '$senha')";
    
    $resultado_usuario = mysqli_query($conn, $result_usuario);

?>
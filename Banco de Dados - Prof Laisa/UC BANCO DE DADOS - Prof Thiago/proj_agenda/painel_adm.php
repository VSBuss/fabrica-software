<?php
  session_start();
?>


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MENU ADMINISTRATIVO</title>
    <link rel="stylesheet" href="./style/estilo_adm.css">
</head>

<body>

    <header class = "header">
        <nav class = "nav-bar">
            <div class="imagem-logo"> 
            <a href="index.html"><img src="./pictures/img_adm/logo senac hub.png" alt="Carregando.." class="logo" ></a></div>
            
            
           
            <div class = "hamburguer">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
                <img src="./pictures/img_adm/senac.png" alt="" class="logo2">
          
        </nav>
    </header>

    <div class="botao">

        <div class="botoes">
            <a href="agenda.php">  <button class="botao-agenda"> <h2> AGENDA </h2> </button> </a>
        </div>
        <div class="botoes">
            <a href="lista_agenda.php">  <button class="botao-agenda"> <h2> AGENDADOS </h2> </button> </a>
        </div>
    
    
        <div class="botoes">
            <a href="servicos.php">  <button class="botao-agenda">  <h2> CADASTRAR SERVIÇOS </h2> </button> </a>
        </div>
    
        <div class="botoes">
            <a href="clientes.php">  <button class="botao-agenda">   <h2> CADASTRAR CLIENTES </h2> </button> </a>
        </div>
    
        <div class="botoes">
            <a href="profissionais.php">  <button class="botao-agenda">   <h2> CADASTRAR PROFISSIONAIS </h2> </button> </a>
        </div>
    
    </div>
</body>

</html>
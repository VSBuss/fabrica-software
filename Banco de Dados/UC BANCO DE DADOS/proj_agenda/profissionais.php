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
	<link rel="stylesheet" href="./style/estilo_profissionais.css">

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
        <a href="lista_agenda.html">  <button class="botao-agenda"> <h2> AGENDADOS </h2> </button> </a>
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

<div class="container">

    <form class="card">

        <div class="card-content">

            <h2>CADASTRAR PROFISSIONAIS</h2>

            <div class="card-content-area">

                <label for="nome">NOME COMPLETO:</label>

                <input type="text" id="nome" autocomplete="off">

            </div>

            <div class="card-content-area">

                <label for="especialidade">ESPECIALIDADE:</label>

                <input type="text" id="especialidade" autocomplete="off">

            </div>

            <div class="card-content-area">

                <label for="sexo">SEXO: </label>

               <select name="sexo" id="sexo">
                <option value="X" >Selecione o Sexo</option>
                <option value="M" >Masculino</option>
                <option value="F" >Feminino</option>
                <option value="O" >Outros</option>
               </select>

            </div>

  

        <div class="card-content-area">

            <label for="turma">TURMA:</label>

            <input type="text" id="turma" autocomplete="off">

        </div>

      

        <div class="card-footer">

                <input type="button" value="ENTRAR" class="button">

        </div>

    </form>


</div>
 
</body>
</html>
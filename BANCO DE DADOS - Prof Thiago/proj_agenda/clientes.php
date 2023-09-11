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
    <?php
            if(isset($_SESSION['msg'])){
              echo($_SESSION['msg']);
              unset($_SESSION['msg']);
            }
            ?>
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

<div class="container">

    <form class="card" action= "">

        <div class="card-content">

            <h2>CADASTRAR CLIENTES</h2>

            <div class="card-content-area">

                <label for="nome">NOME COMPLETO:</label>

                <input type="text" id="nome" autocomplete="off">

            </div>

            <div class="card-content-area">

                <label for="cpf">CPF:</label>

                <input type="number" id="cpf" name="cpf" autocomplete="off">

            </div>

            <div class="card-content-area">

                <label for="data_nasc">DATA DE NASCIMENTO:</label>

                <input type="date" id="data_nasc" name="data_nasc" autocomplete="off">

            </div>

            <div class="card-content-area">

                <label for="sexo">SEXO: </label>

               <select name="sexo" id="sexo">
                <option value="X" disabled selected>Selecione o Sexo</option>
                <option value="M" >Masculino</option>
                <option value="F" >Feminino</option>
                <option value="O" >Outros</option>
               </select>

            </div>

  

        <div class="card-content-area">

            <label for="fone">TELEFONE:</label>

            <input type="number" id="fone" name="fone" autocomplete="off">

        </div>

        <div class="card-content-area">

            <label for="endereco">ENDEREÇO:</label>

            <input type="text" id="endereco" name="endereco" autocomplete="off">

        </div>

        <div class="card-content-area">

            <label for="email">E-MAIL:</label>

            <input type="email" id="email" name="email" autocomplete="off">

        </div>


        <div class="card-content-area">

            <label for="senha">SENHA:</label>

            <input type="password" id="senha" name="senha" autocomplete="off">

        </div>

      

        <div class="card-footer">


                <input type="button" value="ENTRAR" class="button">

        </div>

    </form>


</div>
 
</body>
</html>
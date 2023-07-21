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
	<link rel="stylesheet" href="./style/estilo_agenda.css">

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
        <a href="lista_agenda.php">  <button class="botao-agenda"> <h2> CLIENTES AGENDADOS </h2> </button> </a>
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

</div>

<div class="container">

    <form class="card" method="POST" action="processo-agenda.php">

        <div class="card-content">

            <h2>AGENDAR ATENDIMENTO</h2>

            <div class="card-content-area">

                <label for="data">DATA:</label>

                <input type="date" id="data" name="data" autocomplete="off">

            </div>


            <div class="card-content-area">

                <label for="hora">HORÁRIO:</label>

                <input type="time" id="hora" name="hora" autocomplete="off">

            </div>

            <div class="card-content-area">

                <label for="servico">SERVIÇO:</label>

                <select name="servico" id="servico">
                    <option value="X"> Selecione o Serviço </option>
                    <option value="Manicure">Barbearia</option>
                    <option value="Manicure">Manicure</option>
                    <option value="Manicure">Pedicure</option>
                    <option value="Manicure">Corte de Cabelo</option>
                    <option value="Manicure">Design de Sobrancelha</option>
                    <option value="Manicure">Extensão de Cílios</option>
                    <option value="Manicure">Maquiagem</option>
                    <option value="Manicure">Podologia</option>
                    <option value="Manicure">Massoterapia</option>
                </select>

            </div>

            <div class="card-content-area">

                <label for="profissional">PROFISSIONAL:</label>

                <select name="profissional" id="profissional">
                    <option value="X"> Selecione o Profissional </option>
                    <option value="Maria">Maria</option>
                    <option value="João">João</option>
                    
                </select>

            </div>
       

        <div class="card-footer">

            <input type="submit" value="CADASTRAR" class="button">

        </div>

    </form>


</div>
 
</body>
</html>
<?php
include "conexao.php";
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MENU ADMINISTRATIVO</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
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
        <a href="agenda.php">  <button class="botao-agenda"> <h2 class ="nome-botao"> AGENDA </h2> </button> </a>
    </div>
    <div class="botoes">
        <a href="lista_agenda.php">  <button class="botao-agenda"> <h2 class ="nome-botao"> AGENDADOS </h2> </button> </a>
    </div>


    <div class="botoes">
        <a href="servicos.php">  <button class="botao-agenda">  <h2 class ="nome-botao"> CADASTRAR SERVIÇOS </h2> </button> </a>
    </div>

    <div class="botoes">
        <a href="clientes.php">  <button class="botao-agenda">   <h2 class ="nome-botao"> CADASTRAR CLIENTES </h2> </button> </a>
    </div>

    <div class="botoes">
        <a href="profissionais.php">  <button class="botao-agenda">   <h2 class ="nome-botao"> CADASTRAR PROFISSIONAIS </h2> </button> </a>
    </div>

</div>

<div class="container">
        <h2 class="text-center"> LISTA DE CLIENTES AGENDADOS </h2>
        <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">cliente</th>
                <th scope="col">data</th>
                <th scope="col">hora</th>
                <th scope="col">serviço</th>
                <th scope="col">profissional</th>
              </tr>
            </thead>
            <tbody>
              <?php
              $sql= "SELECT * FROM agendamento LIMIT 10";
              $result =mysqli_query($conn,$sql);
              if($result){
                while($row = mysqli_fetch_assoc($result)){
                  $cliente = $row['idcliente'];
                  $data = $row['data_agenda'];
                  $hora = $row['hora'];
                  $servico = $row['idservico'];
                  $profissional = $row['idatentende'];

                  echo '
                  <tr>
                <th scope="row">  '.$cliente.' </th>
                <td> '.$data. ' </td>
                <td> '.$hora.'</td>
                <td>'.$servico.'</td>
                <td>'.$profissional.'</td>
              </tr>
                  ';

                }
              }


            ?>
              
            </tbody>
          </table>
   

</div>
 
</body>
</html>
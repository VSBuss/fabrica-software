<?php
   
    include_once("conexao.php");

    $idcliente = filter_input(INPUT_POST, 'cliente');
    $data_agenda = filter_input(INPUT_POST, 'data');
    $hora = filter_input(INPUT_POST, 'hora');
    $idservico = filter_input(INPUT_POST, 'servico');
    $idatentende = filter_input(INPUT_POST, 'profissional');



    $result_agenda = "INSERT INTO agendamento (data_agenda, hora, idcliente, idservico, idatentende)
     VALUES ('$data_agenda', '$hora', '$idcliente', '$idservico', '$idatentende')";





    $resultado_agenda = mysqli_query($conn, $result_agenda);

?>
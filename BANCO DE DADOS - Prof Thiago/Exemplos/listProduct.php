<?php 
include 'connect.php';

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>lisProduct</title>
</head>
<body>
<table>
    <thead>
        <tr>
            <th>#id</th>
            <th>#nome</th>
            <th>#descricao</th>
            <th>#quantidade</th>
        </tr>
    </th>
</thead>
<tbody>
<?php 
    $sql = 'SELECT * FROM produto';
    $result = mysqli_query($conn,$sql);

    if($result){
        //var_dump($result);
        while($row=mysqli_fetch_assoc($result)){
            $id = $row['id_produto'];
            $nome = $row['nome'];
            $desc = $row['descricao'];
            $preco = $row['preco'];
            $qtde = $row['qtde'];

            echo '
                <tr>
                <td>'.$id.'</td>
                <td>'.$nome.'</td>
                <td>'.$desc.'</td>
                <td>'.$preco.'</td>
                <td>'.$qtde.'</td>
                <td><a href="delete_prod.php?deleteid='.$id.'">X</a></td>
                </tr>
            ';



        }
    }


?>
</tbody>
</table>


</body>
</html>
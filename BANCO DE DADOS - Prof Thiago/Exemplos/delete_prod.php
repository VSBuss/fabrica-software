<?php 
include 'connect.php';
if(isset($_GET['deleteid'])){
    $id = $_GET['deleteid'];
    echo "id: $id";

    $sql="DELETE FROM produto WHERE id_produto=$id";
    $result=mysqli_query($conn,$sql);
}
?>
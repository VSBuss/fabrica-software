<!DOCTYPE html>
<html>

<head>
    <title>Lista de Usuários</title>
    <link rel="stylesheet" type="text/css" href="../public/css/style.css">
</head>

<body>
    <h1>CRUD Users</h1>
    <a href="index.php?action=create">Cadastrar Novo Usuário</a> <br><br>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
        <?php foreach ($users as $user) : ?>
            <tr>
                <td><?php echo $user['id']; ?></td>
                <td><?php echo $user['name']; ?></td>
                <td><?php echo $user['email']; ?></td>
                <td>
                    <a href="index.php?action=edit&id=<?php echo $user['id']; ?>">Edit</a>
                    <a href="index.php?action=delete&id=<?php echo $user['id']; ?>">Delete</a>
                </td>
            </tr>
        <?php endforeach; ?>
    </table>
</body>

</html>
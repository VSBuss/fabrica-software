<!DOCTYPE html>
<html>

<head>
    <title>Edit User</title>
    <link rel="stylesheet" type="text/css" href="../public/css/style.css">
</head>

<body>
    <h1>Edit User</h1>
    <form method="POST" action="index.php?action=edit&id=<?php echo $user['id']; ?>">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo $user['name']; ?>" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?php echo $user['email']; ?>" required>

        <input type="submit" value="Editar">
    </form>
</body>

</html>
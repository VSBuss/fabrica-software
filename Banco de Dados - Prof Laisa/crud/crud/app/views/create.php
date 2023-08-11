<!DOCTYPE html>
<html>

<head>
    <title>Create User</title>
    <link rel="stylesheet" type="text/css" href="../public/css/style.css">
</head>

<body>
    <h1>Create User</h1>
    <form method="POST" action="index.php?action=create">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <input type="submit" value="Salvar">
    </form>
</body>

</html>
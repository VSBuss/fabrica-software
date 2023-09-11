<?php
require_once 'config/config.php';
require_once 'app/controllers/UserController.php';

$userController = new UserController($pdo);

if (isset($_GET['action'])) {
    $action = $_GET['action'];
    switch ($action) {
        case 'create':
            $userController->create();
            break;
        case 'edit':
            if (isset($_GET['id'])) {
                $id = $_GET['id'];
                $userController->edit($id);
            } else {
                // Página não encontrada
            }
            break;
        case 'delete':
            if (isset($_GET['id'])) {
                $id = $_GET['id'];
                $userController->delete($id);
            } else {
                // Página não encontrada
            }
            break;
        default:
            // Página não encontrada
            break;
    }
} else {
    $userController->index();
}

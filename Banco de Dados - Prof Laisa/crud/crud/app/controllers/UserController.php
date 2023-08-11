<?php
//require_once '../models/User.php';
require_once 'app/models/User.php';

class UserController
{
    public $userModel;

    public function __construct($pdo)
    {
        $this->userModel = new User($pdo);
    }

    public function index()
    {
        $users = $this->userModel->getAllUsers();
        require_once 'app/views/index.php';
    }

    public function create()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $name = $_POST['name'];
            $email = $_POST['email'];
            $this->userModel->createUser($name, $email);
            header('Location: index.php');
            exit;
        }
        require_once 'app/views/create.php';
    }

    public function edit($id)
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $name = $_POST['name'];
            $email = $_POST['email'];
            $this->userModel->updateUser($id, $name, $email);
            header('Location: index.php');
            exit;
        }
        $user = $this->userModel->getUserById($id);
        require_once 'app/views/edit.php';
    }

    public function delete($id)
    {
        $this->userModel->deleteUser($id);
        header('Location: index.php');
        exit;
    }
}

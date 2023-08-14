<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cadastro Usuário</title>
        <link rel="stylesheet" href="../../css/gestor/cadastro.css">
</head>
<body>
    <?php include_once("menu.php") ?>
    <!--TELA CADASTRO DE USUÁRIOS MARINÊS-->
    <div class="caduser">
        <div class="caixa-input">
            <input required="" type="text" class="input">
            <span class="barra"></span>
            <label class="label">
            <span class="label-letra" style="--index: 0">N</span>
            <span class="label-letra" style="--index: 1">O</span>
            <span class="label-letra" style="--index: 2">M</span>
            <span class="label-letra" style="--index: 3">E</span>
            </label>
        </div>
        <div class="caixa-input">
            <input required="" type="text" class="input">
            <span class="barra"></span>
            <label class="label">
            <span class="label-letra" style="--index: 0">E</span>
            <span class="label-letra" style="--index: 1">-</span>
            <span class="label-letra" style="--index: 2">M</span>
            <span class="label-letra" style="--index: 3">A</span>
            <span class="label-letra" style="--index: 4">I</span>
            <span class="label-letra" style="--index: 5">L</span>
            </label>
        </div>
        <div class="caixa-input">
            <input required="" type="text" class="input">
            <span class="barra"></span>
            <label class="label">
            <span class="label-letra" style="--index: 0">C</span>
            <span class="label-letra" style="--index: 1">P</span>
            <span class="label-letra" style="--index: 2">F</span>
            </label>
        </div>
        
        <div class="foto">
            <span>Inserir imagem</span>
            <input type="file" name="foto" id="foto">
        </div>
    
        <div class="radio-button">
            <input class="option1" name="example-radio" type="radio">
            <span class="radio"></span>
            <span class="textoradio">Colaborador</span>
        </div>
        
        <div class="radio-button">
            <input class="option2" name="example-radio" type="radio">
            <span class="radio"></span>
            <span class="textoradio">Gestor</span> 
        </div>
        <input class="check" type="checkbox" id="checkbox_toggle">
        
    
            <div class="checkbox">
            <label for="checkbox_toggle" class="slide">
                <label for="checkbox_toggle" class="toggle"></label>
                <label for="checkbox_toggle" class="text">Ativo</label>
                <label for="checkbox_toggle" class="text">Inativo</label>
            </label>
            </div>
    
    
        <div class=botao>
            <input class= "btncads" type="submit" value="Cadastrar">
            <input class= "btncads" type="submit" value="Editar">
            <input class= "btncads" type="submit" value="Salvar">
        </div>
    </div>
</body>
</html>
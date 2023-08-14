<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Produtos</title>
    <link rel="stylesheet" href="../../css/gestor/cadastro.css">
</head>
<body>
    <?php include_once("menu.php") ?>
    <!--TELA CADASTRO DE PRODUTOS MARINÊS-->
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
            <span class="label-letra" style="--index: 0">D</span>
            <span class="label-letra" style="--index: 1">E</span>
            <span class="label-letra" style="--index: 2">S</span>
            <span class="label-letra" style="--index: 3">C</span>
            <span class="label-letra" style="--index: 4">R</span>
            <span class="label-letra" style="--index: 5">I</span>
            <span class="label-letra" style="--index: 3">Ç</span>
            <span class="label-letra" style="--index: 4">Ã</span>
            <span class="label-letra" style="--index: 5">O</span>
            </label>
        </div>
        <div class="caixa-input">
            <input required="" type="text" class="input">
            <span class="barra"></span>
            <label class="label">
            <span class="label-letra" style="--index: 0">C</span>
            <span class="label-letra" style="--index: 1">U</span>
            <span class="label-letra" style="--index: 0">S</span>
            <span class="label-letra" style="--index: 1">T</span>
            <span class="label-letra" style="--index: 2">O</span>
            </label>
        </div>
        <div class="caixa-input">
            <input required="" type="text" class="input">
            <span class="barra"></span>
            <label class="label">
            <span class="label-letra" style="--index: 0">V</span>
            <span class="label-letra" style="--index: 1">A</span>
            <span class="label-letra" style="--index: 2">L</span>
            <span class="label-letra" style="--index: 0">O</span>
            <span class="label-letra" style="--index: 1">R</span>
            </label>
        </div>
            
            
        <div class="foto">
            <span>Inserir imagem</span>
            <input type="file" name="foto" id="foto">
        </div>
    
        <input class="check" type="checkbox" id="checkbox_toggle">
            <div class="checkbox">
                <label for="checkbox_toggle" class="slide">
                <label for="checkbox_toggle" class="toggle"></label>
                <label for="checkbox_toggle" class="text">Ativo</label>
                <label for="checkbox_toggle" class="text">Inativo</label>
                </label>
            </div>
    
        <div class=botaop>
            <input class= "btncads" type="submit" value="Cadastrar">
            <input class= "btncads" type="submit" value="Editar">
            <input class= "btncads" type="submit" value="Salvar">
        </div>
    </div>
</body>
</html>
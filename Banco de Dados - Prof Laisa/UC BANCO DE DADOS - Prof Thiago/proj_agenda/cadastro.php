<?php
  session_start();
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilo.css">
    <title>Cadastro Senac</title>
</head>
<body class="log-entrar">
    <div class="container" >
        <a class="links" id="paracadastro"></a>
        <a class="links" id="paralogin"></a>
        
        <div class="content">      
          <div id="login">
          <?php
            if(isset($_SESSION['msg'])){
              echo($_SESSION['msg']);
              unset($_SESSION['msg']);
            }
            ?>
            <form method="post" action="processo_cadastro.php"> 
              <h1>Login</h1> 
              <p> 
                <label for="email_login">E-mail</label>
                <input id="email_login" name="email_login" required="required" type="text" placeholder="usuario@fulano.com"/>
              </p>
 
              <p> 
                <label for="senha_login"> Senha</label>
                <input id="senha_login" name="senha_login" required="required" type="password" placeholder="123456" /> 
              </p>
              
              <p> 
                <input type="checkbox" name="manterlogado" id="manterlogado" value="" /> 
                <label for="manterlogado">Manter-me logado</label>
              </p>
              
              <p> 
                <input type="submit" value="Entrar" /> 
              </p>
              
              <p class="link">
                Ainda não tem conta?
                <a href="#paracadastro">Cadastre-se</a>
              </p>
            </form>
          </div>
    
          <div id="cadastro">
            <form method="POST" action="processo_cadastro.php"> 
              <h1>Cadastro</h1> 
              
              <p> 
                <label for="nome_cad">Nome</label>
                <input id="nome_cad" name="nome_cad" required="required" type="text" placeholder="Ex: Thalis Carvalho" />
              </p>

              <p> 
                <label for="cpf">cpf</label>
                <input id="cpf" name="cpf" required="required" type="text" placeholder="Ex: 000.000.000-00" />
              </p>


              <p> 
                <label for="data_nasc">Data de Nascimento</label>
                <input id="data_nasc" name="data_nasc" required="required" type="date" />
              </p>

              <p> 
                <label for="data_nasc">Sexo</label>
                <select name="sexo" id="sexo">
                  <option value="X" selected disabled>Selecione o Sexo</option>
                  <option value="M" selected disabled>Masculino</option>
                  <option value="F" selected disabled>Feminino</option>
                  <option value="O" selected disabled>Outro</option>
                </select>
              </p>

              <p> 
                <label for="fone">Telefone</label>
                <input id="fone" name="fone" required="required" type="number" placeholder="67 99999-9999"/> 
              </p>

              <p> 
                <label for="endereco">Endereço</label>
                <input id="endereco" name="endereco" required="required" type="text" placeholder="Av. Afonso Pena, 4400"/> 
              </p>
              
              <p> 
                <label for="email_cad"> E-mail</label>
                <input id="email_cad" name="email_cad" required="required" type="email" placeholder="usuario@fulano.com"/> 
              </p>
              
              <p> 
                <label for="senha_cad">Senha</label>
                <input id="senha_cad" name="senha_cad" required="required" type="password" placeholder="123456"/>
              </p>
              
              <p> 
                <input type="submit" value="Cadastrar"/> 
              </p>
              
              <p class="link">  
                Já tem conta?
                <a href="#paralogin"> Ir para Login </a>
              </p>
            </form>
          </div>
        </div>
      </div> 
    
</body>
</html>
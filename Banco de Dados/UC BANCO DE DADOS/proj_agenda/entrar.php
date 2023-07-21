<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="estilo.css">
    <title>Login Senac</title>
</head>
<body class="entrar-log">
    <div class="container" >
        <a class="links" id="paracadastro"></a>
        <a class="links" id="paralogin"></a>
        
        <div class="content">      
          <div id="login">
            <form method="post" action=""> 
              <h1>Login</h1> 
              <p> 
                <label for="email_login"> E-mail</label>
                <input id="email_login" name="email_login" required="required" type="text" placeholder="usuario@fulano.com"/>
              </p>
              
              <p> 
                <label for="senha_login">Senha</label>
                <input id="senha_login" name="senha_login" required="required" type="password" placeholder="123456" /> 
              </p>
              
              <p> 
                <input type="checkbox" name="manterlogado" id="manterlogado" value="" /> 
                <label for="manterlogado">Manter-me logado</label>
              </p>
              
              <p> 
                <input type="submit" value="Entrar" /> 
              </p>  
            </form>
          </div>
          


</body>
</html>
<?php include_once("./config/config.php") ?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tela Login</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body class="bodyLogin">

  <img src="img/thiago-removebg.png" alt="Fundo laranja" id="atorLogin">
  <div class="loader">
    <img src="img/0099.png" alt="Moeda" id="moedaFrente">
  </div>
    
  <section id="sectionLogin">
    <div class="imgLogin">
      <img src="img/logo_branca (1).png" alt="..." id="img-login">
    </div>
    <div class="formDiv-login">
      <form class="formLogin" action="" method="post" autocomplete="on">

          <div class="campo">
            <svg class="icons-login" width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M13 1C6.3724 1 1 6.3724 1 13C1 19.6276 6.3724 25 13 25C19.6276 25 25 19.6276 25 13C25 6.3724 19.6276 1 13 1Z" stroke="#D75B36" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M4.59961 21.4001C4.59961 21.4001 5.31477 19.0001 12.9996 19.0001C20.6845 19.0001 21.3996 21.4001 21.3996 21.4001M12.9989 15.7647C14.1106 15.7647 15.1768 15.3346 15.9629 14.569C16.749 13.8034 17.1906 12.7651 17.1906 11.6824C17.1906 10.5997 16.749 9.56135 15.9629 8.79577C15.1768 8.0302 14.1106 7.6001 12.9989 7.6001C11.8872 7.6001 10.821 8.0302 10.0349 8.79577C9.2488 9.56135 8.80718 10.5997 8.80718 11.6824C8.80718 12.7651 9.2488 13.8034 10.0349 14.569C10.821 15.3346 11.8872 15.7647 12.9989 15.7647Z" stroke="#D75B36" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <input type="email" name="login" id="ilogin" placeholder="E-mail"
            autocomplete="email" required maxlength="30" class="inputLogin">
          </div>

          <div class="campo">
            <svg class="icons-login" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18.6974 10.6047C18.2397 10.6047 17.8602 10.2251 17.8602 9.76744V7.53488C17.8602 4.0186 16.8667 1.67442 11.9997 1.67442C7.13275 1.67442 6.13926 4.0186 6.13926 7.53488V9.76744C6.13926 10.2251 5.75973 10.6047 5.30205 10.6047C4.84438 10.6047 4.46484 10.2251 4.46484 9.76744V7.53488C4.46484 4.29767 5.24624 0 11.9997 0C18.7532 0 19.5346 4.29767 19.5346 7.53488V9.76744C19.5346 10.2251 19.1551 10.6047 18.6974 10.6047Z" fill="#D75B36"/>
              <path d="M12 20.0927C10.0018 20.0927 8.37207 18.463 8.37207 16.4648C8.37207 14.4667 10.0018 12.8369 12 12.8369C13.9981 12.8369 15.6279 14.4667 15.6279 16.4648C15.6279 18.463 13.9981 20.0927 12 20.0927ZM12 14.5113C10.9283 14.5113 10.0465 15.3932 10.0465 16.4648C10.0465 17.5364 10.9283 18.4183 12 18.4183C13.0716 18.4183 13.9535 17.5364 13.9535 16.4648C13.9535 15.3932 13.0716 14.5113 12 14.5113Z" fill="#D75B36"/>
              <path d="M17.5814 23.9999H6.4186C1.49581 23.9999 0 22.5041 0 17.5813V15.3488C0 10.426 1.49581 8.93018 6.4186 8.93018H17.5814C22.5042 8.93018 24 10.426 24 15.3488V17.5813C24 22.5041 22.5042 23.9999 17.5814 23.9999ZM6.4186 10.6046C2.42233 10.6046 1.67442 11.3637 1.67442 15.3488V17.5813C1.67442 21.5665 2.42233 22.3255 6.4186 22.3255H17.5814C21.5777 22.3255 22.3256 21.5665 22.3256 17.5813V15.3488C22.3256 11.3637 21.5777 10.6046 17.5814 10.6046H6.4186Z" fill="#D75B36"/>
            </svg>
            <input type="password" name="senha" id="myInput" placeholder="Senha" autocomplete="current-password" requi red minlength="8" maxlength="20" class="inputLogin">
            <!-- <input type="checkbox" onclick="myFunction()"> -->
          </div>
          <a href="esqueci.html" class="botao">Esqueci minha senha.</a>

          <div class="EntrarLogin">
            <input type="submit" value="ENTRAR" class="entrar">
            <svg width="20" height="20" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M39.611 16.083H38V16H20V24H31.303C29.654 28.657 25.223 32 20 32C13.373 32 8 26.627 8 20C8 13.373 13.373 8 20 8C23.059 8 25.842 9.154 27.961 11.039L33.618 5.382C30.046 2.053 25.268 0 20 0C8.955 0 0 8.955 0 20C0 31.045 8.955 40 20 40C31.045 40 40 31.045 40 20C40 18.659 39.862 17.35 39.611 16.083Z" fill="#FFC107"/>
              <path d="M2.30566 10.691L8.87666 15.51C10.6547 11.108 14.9607 8 19.9997 8C23.0587 8 25.8417 9.154 27.9607 11.039L33.6177 5.382C30.0457 2.053 25.2677 0 19.9997 0C12.3177 0 5.65566 4.337 2.30566 10.691Z" fill="#FF3D00"/>
              <path d="M20.0003 40.0002C25.1663 40.0002 29.8603 38.0232 33.4093 34.8082L27.2193 29.5702C25.1439 31.1486 22.6078 32.0023 20.0003 32.0002C14.7983 32.0002 10.3813 28.6832 8.71731 24.0542L2.19531 29.0792C5.50531 35.5562 12.2273 40.0002 20.0003 40.0002Z" fill="#4CAF50"/>
              <path d="M39.611 16.083H38V16H20V24H31.303C30.5142 26.2164 29.0934 28.1532 27.216 29.571L27.219 29.569L33.409 34.807C32.971 35.205 40 30 40 20C40 18.659 39.862 17.35 39.611 16.083Z" fill="#1976D2"/>
            </svg>
          </div>
      </form>
    </div>
  </section>
  <!-- <script>
    function myFunction() {
      var x = document.getElementById("myInput"); Função de mostrar a senha
      if (x.type === "password") {
        x.type = "text";
      } else {
        x.type = "password";
      }
    }
  </script> -->
</body>
</html>
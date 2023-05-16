function actionLogar(){
    var login = "admin@admin.com"
    var senha = "admin123"

    //var usernickmail = window.document.body.getElementsByClassName("nickmail").value
    var input = document.getElementById("nickmail");
    var nickmail = input.value;
    //var usernickmail = elemento.

    var input = document.getElementById("senhord");
    var senhord = input.value;
    //qvar senhord = document.getElementsByClassName("senhord").value
    //var senhord = elemento.value()

    if (login == nickmail && senhord == senha){
        alert("Acesso concedido.")
    }else{
        alert("Login e/ou senha incorretos.")
    }
}
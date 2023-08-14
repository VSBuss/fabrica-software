const menuLateral = document.querySelector(".menulateral"),
cadDropdown = document.getElementById("cadastrarButton"),
subMenu = document.querySelector(".submenu"),
setabaixo = document.querySelector(".setabaixo"),



/*GUILHERME*/
firstcontent = document.querySelector(".firstcontent"),
secondcontent = document.querySelector(".secondcontent"),

listahist = document.querySelector(".lista-historico"),
setabaixa = document.querySelector(".setabaixa");
/*GUILHERME*/

var subMenuAberto = false
var clickCadastrar = false

//método responsável por abrir o menu lateral
menuLateral.addEventListener("click", ()=>{
   //verifica se o clique foi no botão cadastrar
    if(clickCadastrar == false){//se não foi ele abre ou fecha o menu lateral e o sub menu se estiver aberto
        menuLateral.classList.toggle("closed")
        fecharSubMenu()
    }
    else{// se foi ele apenas n faz nada
        clickCadastrar = false // seta como false para validar o proximo clique
    }
})

//método responsável por abrir o sub menu
cadDropdown.addEventListener("click", ()=>{
    //declara que o clique foi no cadastrar
    clickCadastrar = true
    subMenu.classList.toggle("show");
    setabaixo.classList.toggle("rotate");
})

//método responsável por fechar o sub menu
function fecharSubMenu(){
    subMenu.classList.remove("show");
    setabaixo.classList.remove("rotate");
    subMenuAberto = false
}




/*GUILHERME*/
listahist.addEventListener("click", ()=>{
    setabaixa.classList.toggle("rotate");
})

firstcontent.addEventListener("click", ()=>{
    secondcontent.classList.toggle("closed");
})


/*GUILHERME*/
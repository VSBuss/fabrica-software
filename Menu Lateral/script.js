/*
const menuLateral = document.querySelector(".menulateral"),
    cadDropdown = document.querySelector(".cadastrar"),
    subMenu = document.querySelector(".submenu");

    cadDropdown.addEventListener("click", ()=>{
        menuLateral.classList.toggle("closed");
        subMenu.classList.toggle("show");
    })

    menuLateral.addEventListener("click", ()=>{
        menuLateral.classList.toggle("closed");
    })
*/

const menuLateral = document.querySelector(".menulateral");
cadDropdown = document.getElementById("cadastrarButton");
subMenu = document.querySelector(".submenu");

var subMenuAberto = false
var clickCadastrar = false

//metodo responsavel por abrir o menu lateral
menuLateral.addEventListener("click", ()=>{
   //verifica se o clique foi no botão cadastrar
    if(clickCadastrar == false){//se não foi ele abre ou fecha o menulateral e o submenu se estiver aberto
        menuLateral.classList.toggle("closed")
        fecharSubMenu()
    }
    else{// se foi ele apenas n faz nada
        clickCadastrar = false // seta como false para validar o proximo clique
    }


})

//metodo responsavel por abrir o submenu
cadDropdown.addEventListener("click", ()=>{
    //declara que o clique foi no cadastrar
    clickCadastrar = true
    subMenu.classList.toggle("show");
})

//metodo responsavel por fechar o submenu
function fecharSubMenu(){
    subMenu.classList.remove("show");
    subMenuAberto = false
}
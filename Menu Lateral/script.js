const home = document.querySelector(".home"),
    menulateral = home.querySelector(".menulateral"),
    toggle = home.querySelector(".toggle");

    toggle.addEventListener("click", () =>{
        menulateral.classList.toggle("close");
    })

$('.cadastrar').click(function(){
    $('.home .menulateral .listamenu .itemlista .cadastrar .setabaixo').toggleClass("rotate");
});
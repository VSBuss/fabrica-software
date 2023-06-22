const home = document.querySelector(".home"), /*body*/
    menulateral = home.querySelector(".menulateral"), /*nav*/
    toggle = home.querySelector(".toggle"), /**/
    submenu = document.querySelector(".submenu");


    toggle.addEventListener("click", () =>{
        menulateral.classList.toggle("close");
    })





/**/
    submenu.addEventListener("click", dropdown);

    function dropdown(){
        submenu.classList.toggle(".droped");
    }
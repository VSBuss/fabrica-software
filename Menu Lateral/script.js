const home = document.querySelector(".home"), /*body*/
    menuLateral = document.querySelector(".menulateral"), /*nav*/
    toggle = document.querySelector(".itemlista"), /**/
    cadDropdown = document.querySelector(".cadastrar"),
    subMenu = document.querySelector(".submenu");


    if (menuLateral.classList.contains("closed")){
        menuLateral.addEventListener("click", ()=>{
            menuLateral.classList.toggle("");
        })
    } else {
        menuLateral.addEventListener("click", ()=>{
            menuLateral.classList.toggle("closed");
        })
    }

/* https://stackoverflow.com/questions/47106652/get-a-class-width-height-etc
/*
    menuLateral.addEventListener("click", ()=>{
        menuLateral.classList.toggle("closed");
    })

    cadDropdown.addEventListener("click", ()=>{
        if (menuLateral == "closed"){
            null
        } else {
            subMenu.classList.toggle("");
        }
    })


/*
    toggle.addEventListener("click", () =>{
        menuLateral.classList.toggle("closed");
        subMenu.classList.remove('show');
    })
*/


/*
    dropdownBtn.addEventListener('click', function(b){
        b.preventDefault();
        subMenu.classList.toggle('show');
        menuLateral.classList.toggle("closed");
    })
*/
const menuLateral = document.querySelector(".menulateral"),
    cadDropdown = document.querySelector(".cadastrar"),
    subMenu = document.querySelector(".submenu");


    cadDropdown.addEventListener("click", ()=>{
        if(menuLateral !== "closed" && subMenu == "show"){
            subMenu.classList.remove("show");
        } else {
            menuLateral.classList.remove("closed");
            subMenu.classList.toggle("show");
        }
    })


    menuLateral.addEventListener("click", ()=>{
        menuLateral.classList.toggle("closed");
    })


    /*
    menuLateral.addEventListener("click", ()=>{
        menuLateral.classList.toggle("closed");
    })
    clickfora.addEventListener("click", ()=>{
        menuLateral.classList.remove("closed");
        subMenu.classList.remove("show");
    })
    */


    /*
    cadDropdown.addEventListener("click", ()=>{
        if (menuLateral !== "closed"){
            subMenu.classList.toggle("show");
            menuLateral.classList.toggle("closed");
        } else {
            null
        }
    })
    */

    /*
    
    const menuLateral = document.querySelector(".menulateral"),
    cadDropdown = document.querySelector(".cadastrar"),
    subMenu = document.querySelector(".submenu"),
    clickfora = document.querySelector(".menuabertomobile");

    menuLateral.addEventListener("click", ()=>{
        menuLateral.classList.toggle("closed");
    })

    clickfora.addEventListener("click", ()=>{
        menuLateral.classList.remove("closed");
        subMenu.classList.remove("show");        
    })

    cadDropdown.addEventListener("click", ()=>{
        if (menuLateral !== "closed"){
            subMenu.classList.toggle("show");
            menuLateral.classList.toggle("closed");
        } else {
            subMenu.classList.toggle("show");
        }
    })
    
    
    
    
    
    
    
    
    
    
    
    */
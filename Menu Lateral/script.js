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
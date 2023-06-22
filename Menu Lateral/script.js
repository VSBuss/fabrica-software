const home = document.querySelector(".home"), /*body*/
    menuLateral = document.querySelector(".menulateral"), /*nav*/
    toggle = document.querySelector(".toggle"), /**/
    dropdownBtn = document.querySelector(".cadastrar"),
    subMenu = document.querySelector(".submenu");


    toggle.addEventListener("click", () =>{
        menuLateral.classList.toggle("closed");
        subMenu.classList.remove('show');
    })

    dropdownBtn.addEventListener('click', function(e){
        e.preventDefault();
        subMenu.classList.toggle('show');
        menuLateral.classList.toggle("closed");
    })
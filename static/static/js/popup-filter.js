/*Arquivo que lida a visualização do formulário de filtro de funcionários*/

const buttonFilter = document.querySelector(".button-filter");
const formFilter = document.querySelector(".form-filter");
const closePopup = document.querySelector(".close-popup");
buttonFilter.addEventListener("click", () =>{

    formFilter.classList.remove("hidden");
})


closePopup.addEventListener("click", () =>{
    formFilter.classList.add("hidden");
})
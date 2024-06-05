/*Arquivo que lida com a visualização do botão para redefinir a filtragem*/

const buttonReset = document.querySelector(".button-reset");
const inputSearch = document.querySelector(".input-search");

const handleButtonReset = (value) => {
    if(value !== "") {
        buttonReset.classList.replace("hidden", "flex");
    }
    else {
        buttonReset.classList.replace("flex", "hidden");
    }
}
inputSearch.addEventListener("input", (e) =>{
    value = e.target.value
    handleButtonReset(value)
})

document.addEventListener("DOMContentLoaded", () =>{
    value = inputSearch.value;
    handleButtonReset(value)
})


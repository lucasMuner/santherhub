/*Arquivo que lida a visualização do formulário de criação de linha de produção*/

const buttonCreateProductionLine = document.querySelector(".button-create-production-line");
const popupCreateProductionLine = document.querySelector(".popup-create-production-line");
const buttonClosePopupProductionLine = document.querySelector(".button-close-popup-production-line");


buttonCreateProductionLine.addEventListener("click", () =>{
    popupCreateProductionLine.classList.replace("hidden", "flex");
})

buttonClosePopupProductionLine.addEventListener("click", () =>{
    popupCreateProductionLine.classList.replace("flex", "hidden");
})
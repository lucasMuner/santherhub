/*Arquivo que lida a visualização do formulário de disponibilidade*/

const buttonClosePopupAvailableHours = document.querySelector(".button-close-popup-available-hours");
const popupAvailableHours = document.querySelector(".popup-available-hours");
const buttonAvailableHours = document.querySelector(".button-available-hours");


buttonClosePopupAvailableHours.addEventListener("click", () =>{
    popupAvailableHours.classList.replace("flex", "hidden")
})

buttonAvailableHours.addEventListener("click", () =>{
    popupAvailableHours.classList.replace("hidden", "flex")
})
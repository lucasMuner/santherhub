/*Arquivo que lida a visualização do formulário de disponibilidade*/

const buttonAvailableTimes = document.querySelector(".button-available-times");
const popupAvailableTimes = document.querySelector(".popup-available-times");
const buttonCancelAvailableTimes = document.querySelector(".button-cancel-available-times");

buttonAvailableTimes.addEventListener("click", () =>{
    popupAvailableTimes.classList.replace("hidden", "flex");
})
buttonCancelAvailableTimes.addEventListener("click", () =>{
    popupAvailableTimes.classList.replace("flex", "hidden");
})
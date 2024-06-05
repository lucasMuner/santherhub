/*Arquivo que lida a visualização do formulário de alteração de senha*/

const buttonClose = document.querySelector(".button-close");
const buttonCancel = document.querySelector(".button-cancel");
const popupSetPassword = document.querySelector(".popup-set-password");
const buttonSetPassword = document.querySelector(".button-set-password");

buttonClose.addEventListener("click", () =>{
    popupSetPassword.classList.replace("flex", "hidden");
})
buttonCancel.addEventListener("click", () =>{
    popupSetPassword.classList.replace("flex", "hidden");
})

buttonSetPassword.addEventListener("click", () =>{
    popupSetPassword.classList.replace("hidden", "flex");
})
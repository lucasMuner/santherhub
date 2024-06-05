/*Arquivo que lida a visualização do popup de confirmação para deletar linha de produção*/

const buttonDelete = document.querySelector(".button-delete");
const buttonCancel = document.querySelector(".button-cancel");
const popupConfirm = document.querySelector(".popup-confirm");

buttonDelete.addEventListener("click", () =>{
    popupConfirm.classList.replace("hidden", "flex");
})
buttonCancel.addEventListener("click", () =>{
    popupConfirm.classList.replace("flex", "hidden");
})
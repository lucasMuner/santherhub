/*Arquivo que lida a visualização do popup de confirmação para deletar funcionário*/

const popupDeleteEmployee = document.querySelector(".popup-delete-employee");
const buttonDeleteEmployee = document.querySelector(".button-delete-employee");
const buttonCancelDeleteEmployee = document.querySelector(".button-cancel-delete-employee");


buttonDeleteEmployee.addEventListener("click", () =>{
    popupDeleteEmployee.classList.replace("hidden", "flex");
})

buttonCancelDeleteEmployee.addEventListener("click", () =>{
    popupDeleteEmployee.classList.replace("flex", "hidden");
})

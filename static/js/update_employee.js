/*Teste*/
const selectJob = document.querySelector(".select-job");
const popupChangeJob = document.querySelector(".popup-change-job");
const buttonConfirmChangeJob = document.querySelector(".button-confirm-change-job");
let initialJob 

selectJob.addEventListener("change", () =>{
    const job = selectJob.options[selectJob.selectedIndex].innerText;
    if(job !== initialJob){
        popupChangeJob.classList.replace("hidden", "flex");

    }
})

buttonConfirmChangeJob.addEventListener("click", () =>{

})

document.addEventListener("DOMContentLoaded", () =>{
    initialJob = selectJob.options[selectJob.selectedIndex].innerText;
})
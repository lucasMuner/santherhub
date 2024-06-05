/*Arquivo que lida a visualização da sidebar*/

const sidebar = document.querySelector('.sidebar');
document.addEventListener('DOMContentLoaded', function () {
        const toggleButton = document.getElementById('toggleButton');
        
        if(toggleButton) {
            toggleButton.addEventListener('click', function () {
            sidebar.classList.toggle('hidden');
        });
        }
        
});

const buttonCloseAside = document.querySelector(".button-close-sidebar");
buttonCloseAside.addEventListener("click", () =>{
    sidebar.classList.add("hidden");
})
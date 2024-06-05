document.addEventListener("DOMContentLoaded", function() {
    const dropdownToggle = document.getElementById("dropdown-toggle");
    const dropdownMenu = document.getElementById("dropdown-menu");
    const arrowIcon = document.getElementById("arrow");

    dropdownToggle.addEventListener("click", function(event) {
        dropdownMenu.classList.toggle("hidden");
        arrowIcon.classList.toggle("rotate_90_neg");
    });

    // Fechar o menu suspenso se o usuário clicar fora dele
    document.addEventListener("click", function(event) {
        if (!dropdownMenu.contains(event.target) && event.target !== dropdownToggle) {
            dropdownMenu.classList.add("hidden");
            arrowIcon.classList.remove("rotate_90_neg");
        }
    });
});
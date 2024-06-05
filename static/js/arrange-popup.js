document.addEventListener("DOMContentLoaded", () => {
    const buttonsClose = document.querySelectorAll(".button-close");
    const buttonsCancel = document.querySelectorAll(".button-cancel");
    const popupSetArrange = document.querySelector(".popup-set-arrange");
    const buttonsSetArrange = document.querySelectorAll(".button-set-arrange");

    // Adiciona ouvintes de eventos para todos os botões de fechar
    buttonsClose.forEach(button => {
        button.addEventListener("click", () => {
            popupSetArrange.classList.replace("flex", "hidden");
        });
    });

    // Adiciona ouvintes de eventos para todos os botões de cancelar
    buttonsCancel.forEach(button => {
        button.addEventListener("click", () => {
            popupSetArrange.classList.replace("flex", "hidden");
        });
    });

    // Adiciona ouvintes de eventos para todos os botões de definir senha
    buttonsSetArrange.forEach(button => {
        button.addEventListener("click", () => {
            popupSetArrange.classList.replace("hidden", "flex");
        });
    });
});
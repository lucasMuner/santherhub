/*Arquivo que estabelece a interação do carrosel na pagina onde contém a linha de produção*/

const labelsProductionLine = document.querySelector(".labels-production-line").children;
const formProductionLine = document.querySelector(".form-production-line");

for (const label of labelsProductionLine) {
  label.addEventListener("click", () =>{
    
    for(const labelChildren of labelsProductionLine) {
      labelChildren.classList.remove("label-active");
    }
    label.classList.add("label-active");
  })
}

const selectProductionLine = document.querySelector(".select-production-line");

selectProductionLine.addEventListener("change", () =>{  
  option = selectProductionLine.options[selectProductionLine.selectedIndex];
  window.location.pathname = `linha/${option.dataset.slug}`
})



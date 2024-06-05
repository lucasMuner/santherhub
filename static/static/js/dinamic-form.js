/*Arquivo que cuida da manipulação de dados informados no formulário de registro, atualização e perfil(adm). A principal funcionalidade desse arquivo js é o controle de campos acessíveis para cada tipo de cargo*/
const selectJob = document.querySelector(".select-job");
const selectRole = document.querySelector(".select-role");
const fieldClass = document.querySelector(".field-class");
const inputClass = document.querySelector(".input-class");
const selectProductionLine = document.querySelector(".select-production-line")
const fieldCourses = document.querySelector(".field-courses");
const checkboxsCourses = document.querySelectorAll(".checkbox-course");
const buttonGeneratePassword = document.querySelector(".button-generate-password");

const changeForm = () =>{
    const job = selectJob.options[selectJob.selectedIndex].innerText;
    resetField();
    
    if(job){
        if(isJobWithoutClass(job) && isJobWithoutProductionLine(job)) {
            desativeFieldClass();
            desativeProductionLine();

            if(roles.includes(job) || job === "Diretor") {
                
                desativeRole(job === "Diretor"? "Administrador": job);

            }
        }
        else if(isJobWithoutClass(job)) {
            desativeFieldClass()

            if(roles.includes(job)) {
                desativeRole(job);
            }

            if(!isJobsWithMoreThanProductionLine(job)) {
                selectProductionLine.removeAttribute("multiple");
            }
        }
        else if(isJobWithoutProductionLine(job)) {
            desativeProductionLine()
        }
        else {
            selectRole.value = "Normal"
        }
    }       
}
const isJobWithoutProductionLine = (job) => {
    const jobs = ["Diretor", "Administrador", "Aprendiz"];
    return jobs.includes(job);
}
const isJobWithoutClass = (job) =>{
    const jobs = ["Diretor", "Administrador", "Gerente", "Supervisor", "Planejador", "Eletrônico", "Mecânico", "Aprendiz"];
    return jobs.includes(job) || isTecnic(job);
}
const isJobsWithMoreThanProductionLine = (job) => {
    const jobs = ["Gerente", "Supervisor", "Planejador", "Eletrônico", "Mecânico"];
    return jobs.includes(job) || isTecnic(job);
}
const isTecnic = (job) =>{
    const variations = [ "Técnico", "Téc", "Tec", "Tec.", "Téc."];
    const firstWord = job.split(" ")[0];
    return variations.includes(firstWord);
}
const isOperator = (job) =>{
    const variations = ["Operador", "Op.", "Op"];
    const firstWord = job.split(" ")[0];
    return variations.includes(firstWord);
}
const roles = ["Administrador", "Gerente", "Supervisor"];


const desativeRole = (job) =>{
    selectRole.value = job;
    selectRole.disabled = true;
    selectRole.classList.add("input-disabled")
}
const activeRole = () =>{
    selectRole.disabled = false;
    selectRole.classList.remove("input-disabled")
}


const desativeProductionLine = () =>{
    selectProductionLine.disabled = true
    selectProductionLine.classList.add("input-disabled")

    const options = selectProductionLine.options;

    for (let i = 0; i < options.length; i++) {
        options[i].selected = false;
    }
}
const activeProductionLine = () =>{
    selectProductionLine.disabled = false
    selectProductionLine.classList.remove("input-disabled")
}
const desativeFieldClass = () => {
    inputClass.disabled = true;
    inputClass.classList.add("input-disabled");
    inputClass.options[0].selected = true
}
const activeFieldClass = () =>{
    inputClass.disabled = false;
    inputClass.classList.remove("input-disabled");
}

const desativeFieldCourse = () =>{
    fieldCourses.classList.replace("flex", "hidden");
    checkboxsCourses.forEach(checkbox =>{
        checkbox.disabled = true
    })
}
const activeFieldCourse = () =>{
    fieldCourses.classList.replace("hidden", "flex");
    checkboxsCourses.forEach(checkbox =>{
        checkbox.disabled = false
    })
}
const resetField = () => {
    selectProductionLine.setAttribute("multiple", "multiple");
    activeRole()
    activeFieldClass()
    activeProductionLine()
}

document.addEventListener("DOMContentLoaded", changeForm);


function maskPhone(ev) {
    const phone = ev.target;
    const clearPhone = phone.value.replace(/\D/g, "").substring(0, 11);
    const listPhone = clearPhone.split("");
    
    let formatPhone = "";
    if(ev.key !== "Backspace") {
        if(listPhone.length > 0) {
            formatPhone += `(${listPhone.slice(0,2).join("")})`
        }
        
        if(listPhone.length > 2) {
            formatPhone += ` ${listPhone.slice(2,7).join("")}`
        }
        
        if(listPhone.length > 7) {
            formatPhone += `-${listPhone.slice(7,11).join("")}`
        }
        phone.value = formatPhone;
    }
}
document.querySelector(".input-phone").addEventListener("keyup", (ev) => maskPhone(ev));

function gerarUUID() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    const r = Math.random() * 16 | 0;
    const v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

if(buttonGeneratePassword) {
    buttonGeneratePassword.addEventListener("click", (ev) =>{
    ev.preventDefault()
    const inputPassword = document.querySelector(".input-password")
    inputPassword.value = gerarUUID()
})
}


selectJob.addEventListener("change", changeForm)


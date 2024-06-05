/*Arquivo que lida com o popup do funcionário. A obtenção de dados é feito via Ajax. Os campos que aparecem em cada formulário são dinamicos, ou seja, irá aparecer uma determinada informação a depender do cargo do funcionário e de quem está visualizando o popup*/

const buttonsGetEmployee = document.querySelectorAll(".button-get-employee");
const popupShowEmployee = document.querySelector(".popup-show-employee");
const buttonsClosePopup = document.querySelectorAll(".close-popup-employee");
const buttonUpdateEmployee = document.querySelector(".button-update-employee");
const containerInfo = document.querySelector(".container-info");
const containerAvailability = document.querySelector(".container-availability");
const buttonGetInfo = document.querySelector(".button-get-info");
const buttonGetAvailability = document.querySelector(".button-get-availability");
const screenMain = document.querySelector("body > div");



const styleState = {
    "Ativo": "badge-active",
    "Férias": "badge-vacation",
    "Afastado": "badge-distant"
}

const showCardPopup = (data) =>{
    popupShowEmployee.classList.remove("hidden");
    screenMain.classList.remove("min-h-[100vh]");
    screenMain.classList.add("overflow-hidden", "h-[100vh]");
    buttonUpdateEmployee.href = `/funcionario/${data['re']}/atualizar`;
    if((data["role_account"] == "Supervisor" && ["Supervisor", "Gerente", "Administrador"].includes(data["role_employee"])) || (data["role_account"] == "Gerente" && ["Gerente", "Administrador"].includes(data["role_employee"]))) {
        buttonUpdateEmployee.classList.replace("flex", "hidden");        
    }
    else {
        buttonUpdateEmployee.classList.replace("hidden", "flex");   
    }

    createProfileComponent(data);
    createContactsComponent(data);
    createCoursesComponent(data);
    createInfoComponent(data);
    createAvailabilityComponent(data)
}
const createProfileComponent = (data) =>{
    const photoField = document.querySelector(".field-photo");
    photoField.src = data["photo"];

    const nameField = document.querySelector(".field-name");
    nameField.innerText = data["name"]

    const jobField = document.querySelector(".field-job");
    jobField.innerText = data["job"]


}

const createContactsComponent = (data) =>{
    const emailField = document.querySelector(".field-email");

    emailField.innerText = data["email"]

    const phoneField = document.querySelector(".field-phone");
    phoneField.innerText = data["phone"]
}
const createInfoComponent = (data) => {
    const reField = document.querySelector(".field-re");
    const classField = document.querySelector(".field-class");
    const hireDateField = document.querySelector(".field-hire-date");
    const lastVacationsField = document.querySelector(".field-last-vacations");

    reField.innerText = data["re"];

    if(data['class']) {
        classField.innerText = `${data["class"]}`;
    } 
    else {
        classField.innerText = `-`;
    }
    hireDateField.innerText = new Date(data["hire_date"]).toLocaleDateString("pt-BR");
    lastVacationsField.innerText = data["last_vacations"] ? new Date(data["last_vacations"]).toLocaleDateString("pt-BR"): "-";
    

    const stateField = document.querySelector(".field-state");
    stateField.innerText = data["state"]
    stateField.classList.add(styleState[data["state"]])
    stateField.classList.add("px-4", "py-2", "rounded-md");


    const productionLineField = document.querySelector(".field-production-line");
    productionLineField.innerHTML = ""
    if(!["Diretor", "Administrador", "Aprendiz"].includes(data["job"])) {
        if(data['production_line']) {
            data['production_line'].forEach(productionLine =>{
                const badgeProductionLine = document.createElement("li");
                badgeProductionLine.innerText = productionLine
                badgeProductionLine.classList.add("badge-production-line")
                productionLineField.append(badgeProductionLine)
            })
        }else {
            productionLineField.innerText = "Funcionário não está cadastrado em nenhuma linha!"
        }
    }
    else {
        productionLineField.innerText = "Funcionário cadastrado em todas as linhas!"
    }

}

const createCoursesComponent = (data) => {
    
    const containerAllCourses = document.querySelector(".container-all-courses");
    containerAllCourses.innerHTML = ""
    data["all-courses"].forEach(course =>{
        const container = document.createElement("div");
        container.classList.add("flex", "gap-2")
        const courseText = document.createElement("p");
        const icon = document.createElement("img");
        courseText.innerText = course

        if(data["courses"].includes(course)) {
            icon.src = "../static/assets/svg/check.svg";
        }
        else {
            icon.src = "../static/assets/svg/error.svg";
        }

        container.append(icon, courseText)
        containerAllCourses.append(container)
    })

}

for(const buttonGetEmployee of buttonsGetEmployee) {
    buttonGetEmployee.addEventListener('click', () => {
        const re = buttonGetEmployee.id 

        var xhr = new XMLHttpRequest();
        xhr.open('GET', `/funcionario/${re}`, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                showCardPopup(data["employee"])
                
                
        
            } else if (xhr.readyState === 4 && xhr.status !== 200) {
                console.error('Erro na requisição AJAX:', xhr.status);
            }
        };
        xhr.send();
    });
}

for (const buttonClosePopup of buttonsClosePopup) {
    buttonClosePopup.addEventListener("click", () =>{
    popupShowEmployee.classList.add("hidden");
    screenMain.classList.add("min-h-[100vh]");
    screenMain.classList.remove("overflow-hidden", "h-[100vh]");
})
}

const createAvailabilityComponent = (data) => {
    const containerGrid = document.querySelector(".container-availability-grid");
    containerGrid.innerHTML = "";
    const availability = data["availability"]
    if (data["availability_filled"]) {
        containerGrid.classList.remove("text-typography-secondary");
        containerGrid.classList.add("grid-cols-3");
        availability.forEach(day => {
            const nameDay = document.createElement("p");
            nameDay.innerText = day["name"];
            nameDay.classList.add("font-semibold");

            const initialTime = document.createElement("p");
            initialTime.innerText = day["initial_time"]?.split(":").slice(0, 2).join(":") ?? "-";
            initialTime.classList.add("text-center", "font-medium");
            
            const endTime = document.createElement("p")
            endTime.innerText = day["end_time"]?.split(":").slice(0, 2).join(":") ?? "-";
            endTime.classList.add("text-center", "font-medium");
            containerGrid.append(nameDay, initialTime, endTime);
        })
    }
    else {
        containerGrid.classList.add("text-typography-secondary");
        containerGrid.classList.remove("grid-cols-3");
        containerGrid.innerText = "Funcionário ainda não informou disponibilidade"
    }
}   

if(buttonGetInfo) {
    buttonGetInfo.addEventListener("click", () =>{
    containerAvailability.classList.replace("flex", "hidden");
    containerInfo.classList.replace("hidden", "flex");
    buttonGetInfo.classList.add("active-button");
    buttonGetAvailability.classList.remove("active-button");
})
}
if(buttonGetAvailability) {
    buttonGetAvailability.addEventListener("click", () =>{
    containerAvailability.classList.replace("hidden", "flex");
    containerInfo.classList.replace("flex", "hidden");
    buttonGetAvailability.classList.add("active-button");
    buttonGetInfo.classList.remove("active-button");
})

}






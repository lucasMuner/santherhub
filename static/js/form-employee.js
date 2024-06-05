/*Arquivo que lida com o funcionamento do campo fotos dos formuários*/

const inputPhoto = document.querySelector(".input-photo");

inputPhoto.addEventListener("change", () =>{
   
    const photoLocation = document.querySelector(".photo-location");

    if(inputPhoto && inputPhoto.files[0]) {
        reader = new FileReader()

        reader.onload = (e) =>{
            photoLocation.src = e.target.result
        }

        reader.readAsDataURL(inputPhoto.files[0]);
    }
    
})
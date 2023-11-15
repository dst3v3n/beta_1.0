const nombre = document.getElementById("name");
const apellido = document.getElementById("lastname");
const email = document.getElementById("email");
const passw = document.getElementById("passw");
const pass = document.getElementById("pass");
const from = document.getElementById("form");

from.addEventListener('submit', e=>{
    e.preventDefault()
    if(nombre.value.length <3){
        alert("Nombre Muy Corto")
    }
})

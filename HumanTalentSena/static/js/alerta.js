const nombre = document.getElementById("name");
const apellido = document.getElementById("lastname");
const email = document.getElementById("email");
const passw = document.getElementById("passw");
const pass = document.getElementById("pass");
const from = document.getElementById("form");

from.addEventListener('submit', e=>{
    e.preventDefault()
    let entrada = false
    let regexEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/
    if(nombre.value.length <3){
        alert("Nombre Muy Corto")
        entrada = true
    }
    if(apellido.value.length <3){
        alert("Apellido Muy Corto")
        entrada = true
    }
    if(!regexEmail.test(email.value)){
        alert("El Email No Es Valido")
        entrada = true
    }
    if(passw.value.length <8){
        alert("La Contraseña Es Muy Corta")
        entrada = true
    }
    if(pass.value.length <8){
        // alert("La Contraseña Es Muy Corta")
        entrada = true
    }
    if (passw.value !== pass.value) {
        alert("La Contraseña No Es Igual")
        entrada = true
    }
    if(!entrada){
        alert("Registrado Con Exito" )
    }

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/usuarios/views/metodo_post');
    xhr.setRequestHeader('Content-Type', 'application/json');
    const data = {
        nombre : 'juan' ,
        apellido : 'diaz', 
        email : 'jdss@sd.com',
        password : 1235431,
      };
    xhr.send(JSON.stringify(data));

    xhr.onload = () => {
        const response = xhr.response;
        console.log(response);
      };




})

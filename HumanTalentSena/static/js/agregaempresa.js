const contenedor1 = document.querySelector('#edu1');
const btnAgregar1 = document.querySelector('#agregar1');

// Counter variable
let total1 = 1;

// Function to add new form
btnAgregar1.addEventListener('click', (event) => {
  event.preventDefault();

  const newForm = document.createElement('div');
  newForm.innerHTML = `
  <p class="titulo2">Empresa</p>
  <label for="emp" class="infop">Empresa</label>
  <input type="text" name="Nombre_empresa${total++}" class="inp" maxlength="50" required="" id="id_Nombre_empresa">
  <label for="car" class="infop" id="car">Cargo</label>
  <input type="text" name="Cargo${total++}" class="inp" maxlength="50" required="" id="id_Cargo">
  <br>
  <br>
  <label for="fechai" class="infop">Fecha de inicio</label>
  <input type="date" name="Fecha_Inicio${total++}" class="inp2" required="" id="id_Fecha_Inicio">
  <label for="fechaf" class="infop">Fecha de FInalización</label>
  <input type="date" name="Fecha_Finalizacion${total++}" class="inp2" required="" id="id_Fecha_Finalizacion">
  <br>
  <br>
  <label for="dsr" class="infop">Describa sus fuciones</label>
  <textarea name="Funciones${total++}" cols="40" rows="10" id="dsr" required=""></textarea>
  <br>
  <br>
  <br>
  <button onclick="eliminar1(this)" style="
    background-color: red;
    border-color: black;
    border-radius: 15px;
    font-size: 16px;
    font-weight: bold;
    color: white;
    padding: 10px;
    cursor: pointer;
    ">Eliminar</button>
  `;

  contenedor1.appendChild(newForm);
});

// Function to remove form
function eliminar1(element) {
  const parentNode = element.parentNode;
  contenedor1.removeChild(parentNode);
  actualizarContador();
};

// Function to update counter
function actualizarContador() {
  const forms = contenedor1.children;
  total1 = 1;

  for (let i = 0; i < forms.length; i++) {
    forms[i].children.innerHTML = total++;
  }
};

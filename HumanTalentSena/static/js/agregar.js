const contenedor = document.querySelector('#edu');
const btnAgregar = document.querySelector('#agregar');

// Counter variable
let total = 1;

// Function to add new form
btnAgregar.addEventListener('click', (event) => {
  event.preventDefault();

  const newForm = document.createElement('div');
  newForm.innerHTML = `
    <p class="titulo2">Institución</p>
    <label for="titulo" class="infop">Titulo obtenido</label>
    <input type="file" name="Archivo${total++}" class="inp3" accept=".pdf" id="img" required>
    <label for="cole" class="infop" id="col">Institución</label>
    <input type="text" name="Nombre_Instituto${total++}" class="inp" maxlength="50" required="" id="id_Nombre_Instituto">
    <br>
    <br>
    <label for="añ" class="infop">Año de gradución</label>
    <input type="date" name="Ano_graduacion${total++}" class="inp2" required="" id="id_Ano_graduacion">
    <label for="tim" class="infop" id="tie">timpo en la institucion</label>
    <input type="number" name="Tiempo${total++}" class="inp1" required="" id="id_Tiempo">
    <br>
    <br>
    <br>
    <button onclick="eliminar(this)" style="
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

  contenedor.appendChild(newForm);
});

// Function to remove form
function eliminar(element) {
  const parentNode = element.parentNode;
  contenedor.removeChild(parentNode);
  actualizarContador();
};

// Function to update counter
function actualizarContador() {
  const forms = contenedor.children;
  total = 1;

  for (let i = 0; i < forms.length; i++) {
    forms[i].children.innerHTML = total++;
  }
};

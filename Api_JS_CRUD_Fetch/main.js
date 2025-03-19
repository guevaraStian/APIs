const grupo_lista = document.querySelector('.grupo_lista');
// Obtienen todos los botones
const obtener_informacion = document.querySelector('.obtener_informacion');
const agregar_informacion = document.querySelector('.agregar_informacion');
const editar_informacion = document.querySelector('.editar_informacion');
const eliminar_informacion = document.querySelector('.eliminar_informacion');

const url = 'https://jsonplaceholder.typicode.com/posts';
let respuesta_pantalla = '';

const obetenerRespuesta = response => response.json();
const procesoJSON = json => {
  if(!!Object.keys(json).length) {
    respuesta_pantalla = `
      <li class="grupo_lista-item">${json.title}</li>
      <li class="grupo_lista-item">${json.body}</li>
    `
  }
  grupo_lista.innerHTML = respuesta_pantalla;
}
const writeServer = (action, data) => ({
  method: action,
  body: JSON.stringify(data),
  headers: {
    'Content-Type': 'application/json; charset=UTF-8'
  }
});

// GET
obtener_informacion.addEventListener('click', () => {
  fetch(`${url}/1`)
    .then(obetenerRespuesta)
    .then(procesoJSON)
});

// POST
agregar_informacion.addEventListener('click', () => {
  const nueva_informacion = {
    userId: 1,
    title: 'Se adiere una informacion',
    body: 'asi se adiere informacion nueva'
  }

  fetch(url, writeServer('POST', nueva_informacion))
    .then(obetenerRespuesta)
    .then(procesoJSON);
});

// PUT
editar_informacion.addEventListener('click', () => {
  const editada_informacion = {
    userId: 2,
    title: 'Editar informacion',
    body: 'Con este boton se edita la informacion'
  }
  fetch(`${url}/1`, writeServer('PUT', editada_informacion))
    .then(obetenerRespuesta)
    .then(procesoJSON);
});

// DELETE
eliminar_informacion.addEventListener('click', () => {
  fetch(`${url}/1`, { method: 'DELETE' })
    .then(obetenerRespuesta)
    .then(procesoJSON);
});
const API_URL = 'http://jsonplaceholder.typicode.com'
const HTMLResponse = document.querySelector("#app");
const ul = document.createElement("ul");

fetch('${API_URL}/users')
    .then((response) => response.json())
    .then((users) =>{
        const tpl = users.map((user) => '<li>${user.name} & ${user.email}</li>');
        HTMLResponse.innerHTML= '<ul>${tpl}</ul>';
    })  











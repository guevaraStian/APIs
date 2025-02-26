const API_URL = 'http://jsonplaceholder.typicode.com'
const HTMLResponse = document.querySelector("#app");
const ul = document.createElement("ul");

fetch('${API_URL}/users')
    .then((response) => response.json())
    .then((users) => {
        user.forEach((user) => {
            let elem = document.createElement("li");
            elem.appendChild(
                document.createTextNode('$[user.name] $[user.email]')



            );
            ul.appendChild(elem);
        });

        HTMLResponse.appendChild(ul)

    });










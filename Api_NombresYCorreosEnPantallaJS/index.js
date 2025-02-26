const API_URL = "http://jsonplaceholder.typicode.com";
const xhr = new XMLHttpRequest();


function onRequesHandler() {
    if (this.readyState == 4 && this.status == 200){
        console.log(this.response);
    }
}
xhr.addEventListener("load", onRequesHandler);
xhr.open("GET", '${API_URL}/users');
xhr.send();











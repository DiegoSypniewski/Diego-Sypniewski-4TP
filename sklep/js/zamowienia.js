const miasta=[

"Warszawa",
"Kraków",
"Poznań",
"Wrocław"

];


document
.querySelector("form")

.addEventListener("submit", e => {

e.preventDefault();

const email =
document.getElementById("email");

if(!email.value.includes("@")){

alert("Błędny email");

return;

}

fetch("https://jsonplaceholder.typicode.com/posts", {

method: "POST",

headers: {
"Content-Type": "application/json"
},

body: JSON.stringify({

email: email.value

})

})

.then(response => response.json())

.then(data => {

alert("Zamówienie zostało złożone!");

console.log(data);

})

.catch(error => {

alert("Błąd podczas składania zamówienia");

console.log(error);

});

});
function pobierzKoszyk(){
return JSON.parse(localStorage.getItem("koszyk")) || [];
}

function zapiszKoszyk(koszyk){
localStorage.setItem("koszyk", JSON.stringify(koszyk));
}

function dodajDoKoszyka(id){

let koszyk = pobierzKoszyk();

let produkt = window.produkty.find(p => p.id === id);

if(!produkt){
console.log("Brak produktu");
return;
}

let istnieje = koszyk.find(p => p.id === id);

if(istnieje){
istnieje.ilosc++;
} else {
koszyk.push({
id: produkt.id,
nazwa: produkt.nazwa,
cena: produkt.cena,
ilosc: 1
});
}

zapiszKoszyk(koszyk);

pokazLiczbeProduktow();

alert("Dodano do koszyka");
}

function pokazLiczbeProduktow(){

let koszyk = pobierzKoszyk();

let suma = 0;

koszyk.forEach(p => {
suma += p.ilosc;
});

let licznik = document.getElementById("liczba");

if(licznik){
licznik.innerText = suma;
}
}

function wyswietlKoszyk(){

let tabela = document.getElementById("produktyKoszyka");

if(!tabela) return;

let koszyk = pobierzKoszyk();

tabela.innerHTML = "";

let suma = 0;

koszyk.forEach(p => {

suma += p.cena * p.ilosc;

tabela.innerHTML += `
<tr>
<td>${p.nazwa}</td>
<td>${p.cena} zł</td>
<td>${p.ilosc}</td>
<td>${p.cena * p.ilosc} zł</td>
</tr>
`;

});

tabela.innerHTML += `
<tr>
<td colspan="3"><b>Razem</b></td>
<td><b>${suma} zł</b></td>
</tr>
`;
}

document.addEventListener("DOMContentLoaded", () => {
pokazLiczbeProduktow();
wyswietlKoszyk();
});
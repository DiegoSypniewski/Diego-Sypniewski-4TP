function wyswietlProdukty(lista){

let kontener = document.getElementById("produktyLista");

if(!kontener) return;

kontener.innerHTML = "";

lista.forEach(p => {

kontener.innerHTML += `
<div class="col-md-4">
<div class="card">
<img src="${p.obraz}" class="card-img-top">
<div class="card-body">
<h5>${p.nazwa}</h5>
<p>${p.cena} zł</p>

<button class="btn btn-success"
onclick="dodajDoKoszyka(${p.id})">
Dodaj do koszyka
</button>

</div>
</div>
</div>
`;

});

}

let szukaj = document.getElementById("szukaj");

if(szukaj){

szukaj.addEventListener("input", e => {

let tekst = e.target.value.toLowerCase();

let wynik = window.produkty.filter(p =>
p.nazwa.toLowerCase().includes(tekst)
);

wyswietlProdukty(wynik);

});

}

wyswietlProdukty(window.produkty);
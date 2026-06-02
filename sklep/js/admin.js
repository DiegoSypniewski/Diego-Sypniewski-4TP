class Admin{

dodajProdukt(){

const nazwa=

document.getElementById("nazwa").value;

const cena=

document.getElementById("cena").value;

if(nazwa.length<3){

alert("Za krótka nazwa");

return;

}

alert("Produkt dodany");

}

}

const admin=new Admin();
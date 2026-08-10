let imagem = document.getElementById("i1")
let p = document.getElementById("t1")
let b1 = document.getElementById("hollow")
let b2 = document.getElementById("Micro")
let b3 = document.getElementById("Gato")

b1.onclick = function(){
    i1.src="imagens/hollow.jpg"
    p.innerHTML = "Muito gente fina vale a pena adotar e cuidar, so tome cuidado ele não gosta de insetos"
}
b2.onclick = function(){
    i1.src="imagens/microondas.jpg"
    p.innerHTML = "Muito versatil, só tome cuidado pois muitos dizem ser radioativo"
}
b3.onclick = function(){
    i1.src="imagens/pokemon.png"
    p.innerHTML = "Pode arranhar, pode de atacar mas sempre vai ser fofinho e um querido para mim"
}
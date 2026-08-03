let cliques = 0
let botao= document.getElementById("Botao-contador")
let h2 = document.getElementById("Contador")
let Botao2 = document.getElementById("reset")
botao.onclick= function(){
    cliques += 1
    h2.innerHTML = cliques
}
Botao2.onclick= function(){
    cliques = 0
    h2.innerHTML = cliques
}
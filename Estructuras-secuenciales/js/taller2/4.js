// Un aprendiz desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales. 30% de la calificación del examen final. 15% de la calificación de un trabajo final.

// entradas
const nota1 = parseFloat(prompt('Ingrese la del primer parcial'))
const nota2 = parseFloat(prompt('Ingrese la del segundo parcial'))
const nota3 = parseFloat(prompt('Ingrese la del tercer parcial'))
const nota4 = parseFloat(prompt('Ingrese la del examen final'))
const nota5 = parseFloat(prompt('Ingrese la del trabajo final'))

// proceso
let resultado1 = (nota1 + nota2 + nota3) / 3 * 0.55
let resultado2 = nota4 * 0.30
let resultado3 = nota5 * 0.15
let resultadoFinal = resultado1 + resultado2 + resultado3

let message = "La calificación final es: "

// salida
console.log(message + resultadoFinal)
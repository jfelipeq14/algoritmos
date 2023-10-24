// Determinar si un número es divisible por otro número.

const numeroUno = parseInt(prompt("Digite el numero 1"))
const numeroDos = parseInt(prompt("Digite el numero 2"))
const modulo = numeroUno % numeroDos

if(modulo !== 0){
  console.log(`El numero ${numeroUno} no es divisible por ${numeroDos}`);
}else{
console.log(`El numero ${numeroUno} si es divisible por ${numeroDos}`);
}

// Determinar si una fecha es válida.

const date = prompt('Digite una fecha')
console.log(date);
// Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario anterior.

const salario = parseInt(prompt("Ingrese el salario del obrero"))
const incremento = salario * 0.25
const nuevoSalario = salario + incremento

alert(`El nuevo salario es ${nuevoSalario}`)
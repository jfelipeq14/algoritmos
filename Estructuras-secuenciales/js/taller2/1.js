// Suponga que un individuo desea invertir su capital (entrada) en un banco y desea saber cuánto dinero ganara (salida) después de un mes si el banco paga a razón de 2% mensual.

const capital = parseInt(prompt("Ingrese el capital a invertir"));
const ganancia = capital * 0.02; // 2% mensual
const total = capital + ganancia;

console.log(`El capital inicial es: ${capital} y la ganancia es de ${ganancia} para un total de ${total}`);
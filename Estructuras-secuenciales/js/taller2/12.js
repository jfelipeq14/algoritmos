// Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.

const inversion1 = parseFloat(prompt("Ingrese la inversión de la primera persona"));
const inversion2 = parseFloat(prompt("Ingrese la inversión de la segunda persona"));
const inversion3 = parseFloat(prompt("Ingrese la inversión de la tercera persona"));

const total = inversion1 + inversion2 + inversion3;

const porcentaje1 = (inversion1 / total) * 100;
const porcentaje2 = (inversion2 / total) * 100;
const porcentaje3 = (inversion3 / total) * 100;

console.log(`El porcentaje de la primera persona es: ${porcentaje1}%`);
console.log(`El porcentaje de la segunda persona es: ${porcentaje2}%`);
console.log(`El porcentaje de la tercera persona es: ${porcentaje3}%`);
// La empresa Salome Style, desea vender 3 productos a “Fredy Lujos”, la empresa a cada producto le da un descuento del 5% al primer producto, al segundo un descuento del 7% y 9% al tercer producto. La empresa “Fredy Lujos” lo contrata para saber cuanto debe pagar por dicha factura.

const producto1 = parseInt(prompt("Ingrese el valor del producto 1"));
let producto1Descuento = producto1 * 0.05;
let producto1Neto = producto1 - producto1Descuento;

const producto2 = parseInt(prompt("Ingrese el valor del producto 2"));
let producto2Descuento = producto2 * 0.07;
let producto2Neto = producto2 - producto2Descuento;

const producto3 = parseInt(prompt("Ingrese el valor del producto 3"));
let producto3Descuento = producto3 * 0.09;
let producto3Neto = producto3 - producto3Descuento;

let totalPago = producto1Neto + producto2Neto + producto3Neto;

console.log("El valor del producto 1 es: " + producto1Neto);
console.log("El valor del producto 2 es: " + producto2Neto);
console.log("El valor del producto 3 es: " + producto3Neto);

console.log("El total a pagar es: " + totalPago);
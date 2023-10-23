// Señor aprendiz el Sena lo contrata para que realice un algoritmo que calcule: venta por producto, valor del IVA, valor descuento y neto a pagar de un cliente para una factura de 5 productos.

const producto1 = parseInt(prompt("Ingrese el valor del producto 1"));
const producto2 = parseInt(prompt("Ingrese el valor del producto 2"));
const producto3 = parseInt(prompt("Ingrese el valor del producto 3"));
const producto4 = parseInt(prompt("Ingrese el valor del producto 4"));
const producto5 = parseInt(prompt("Ingrese el valor del producto 5"));

let valorIva = parseInt(prompt("Ingrese el valor del IVA"));
valorIva = valorIva / 100; // 0.19

let valorDescuento = parseInt(prompt("Ingrese el valor del descuento"));
valorDescuento = valorDescuento / 100; // 0.05

const valorIvaProducto1 = producto1 * valorIva;
const totalProducto1 = producto1 + valorIvaProducto1;
const descuentoProducto1 = totalProducto1 * valorDescuento;
const netoPagar1 = totalProducto1 - descuentoProducto1;

const valorIvaProducto2 = producto2 * valorIva;
const totalProducto2 = producto2 + valorIvaProducto2;
const descuentoProducto2 = totalProducto2 * valorDescuento;
const netoPagar2 = totalProducto2 - descuentoProducto2;

const valorIvaProducto3 = producto3 * valorIva;
const totalProducto3 = producto3 + valorIvaProducto3;
const descuentoProducto3 = totalProducto3 * valorDescuento;
const netoPagar3 = totalProducto3 - descuentoProducto3;

const valorIvaProducto4 = producto4 * valorIva;
const totalProducto4 = producto4 + valorIvaProducto4;
const descuentoProducto4 = totalProducto4 * valorDescuento;
const netoPagar4 = totalProducto4 - descuentoProducto4;

const valorIvaProducto5 = producto5 * valorIva;
const totalProducto5 = producto5 + valorIvaProducto5;
const descuentoProducto5 = totalProducto5 * valorDescuento;
const netoPagar5 = totalProducto5 - descuentoProducto5;

const totalPago = netoPagar1 + netoPagar2 + netoPagar3 + netoPagar4 + netoPagar5;

console.log("El valor del producto 1 es: " + netoPagar1);
console.log("El valor del producto 2 es: " + netoPagar2);
console.log("El valor del producto 3 es: " + netoPagar3);
console.log("El valor del producto 4 es: " + netoPagar4);
console.log("El valor del producto 5 es: " + netoPagar5);

console.log("El total a pagar es: " + totalPago);
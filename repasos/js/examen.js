// Solome lujos tiene clasificados a sus clientes: Tipo A (Bono de 10.000), Tipo B (Bono de 15.000), Tipo C (Bono de 20.000), Tipo D (Bono de 25.000), Tipo E (Bono de 30.000). La empresa John Sadder Styls quiere hacer una compra de varias piezas de la misma clase a una fabrica de refacciones Salome Lujos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagara solicitando un crédito al fabricante. Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagara solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. 

const cantidadPiezas = parseInt(prompt("Digite la cantidad de piezas a comprar")) //11
const precioPieza = parseInt(prompt("Digite el precio de la pieza")) //10000
const tipoCliente = prompt("Digite el tipo de cliente") //a

const subtotal = cantidadPiezas * precioPieza

let dineroPropio = 0
let dineroBanco = 0
let dineroFabricante = 0
let bono = 0

if (tipoCliente === "a") {
    bono = 10000
} else if (tipoCliente === "b") {
    bono = 15000
} else if (tipoCliente === "c") {
    bono = 20000
} else if (tipoCliente === "d") {
    bono = 25000
} else if (tipoCliente === "e") {
    bono = 30000
}

const neto = subtotal - bono

if (neto > 500000) {
    dineroPropio = neto * 0.55
    dineroBanco = neto * 0.30
    dineroFabricante = neto * 0.15
} else if (neto <= 500000) {
    dineroPropio = neto * 0.70
    dineroFabricante = neto * 0.30
}
const intereses = dineroFabricante * 0.20
const credito = dineroFabricante + intereses

console.log(`El subtotal es: ${subtotal}`);
console.log(`El bono es: ${bono}`);
console.log(`El neto es: ${neto}`);
console.log(`El dinero propio a invertir es: ${dineroPropio}`);
console.log(`El dinero del banco para el prestamo es: ${dineroBanco}`);
console.log(`El dinero del fabricante para el credito es: ${dineroFabricante}`);
console.log(`El interes del fabricante (20%) es: ${intereses}`);
console.log(`El dinero del credito al fabricante es: ${credito}`);
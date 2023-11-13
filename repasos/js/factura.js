// hacer un algoritmo que le saque el 18% a una factura si es mas de 10000 y la factura tiene 3 productos, con su codigo, nombre, precio y cantidad y ademas, si la factura es menor de 100000, el descuento es del 9% 

const nombreProducto1 = prompt("Digite el nombre del producto 1")
const codigoProducto1 = prompt("Digite el codigo del producto 1")
const precioProducto1 = parseInt(prompt("Digite el precio del producto 1"))
const cantidadProducto1 = parseInt(prompt("Digite la cantidad del producto 1"))
const totalProducto1 = cantidadProducto1 * precioProducto1

const nombreProducto2 = prompt("Digite el nombre del producto 2")
const codigoProducto2 = prompt("Digite el codigo del producto 2")
const precioProducto2 = parseInt(prompt("Digite el precio del producto 2"))
const cantidadProducto2 = parseInt(prompt("Digite la cantidad del producto 2"))
const totalProducto2 = cantidadProducto2 * precioProducto2


const nombreProducto3 = prompt("Digite el nombre del producto 3")
const codigoProducto3 = prompt("Digite el codigo del producto 3")
const precioProducto3 = parseInt(prompt("Digite el precio del producto 3"))
const cantidadProducto3 = parseInt(prompt("Digite la cantidad del producto 3"))
const totalProducto3 = cantidadProducto3 * precioProducto3

const subtotal = totalProducto1 + totalProducto2 + totalProducto3

let descuento = 0

if (subtotal > 100000) {
    descuento = subtotal * 0.18
} else if (subtotal <= 100000) {
    descuento = subtotal * 0.09
}

const total = subtotal - descuento

console.log(`El producto ${nombreProducto1} tiene un valor de ${precioProducto1} y se compró ${cantidadProducto1} cantidad, entonces el total es ${totalProducto1}`);

console.log(`El producto ${nombreProducto2} tiene un valor de ${precioProducto2} y se compró ${cantidadProducto2} cantidad, entonces el total es ${totalProducto2}`);

console.log(`El producto ${nombreProducto3} tiene un valor de ${precioProducto3} y se compró ${cantidadProducto3} cantidad, entonces el total es ${totalProducto3}`);

console.log(`El subtotal seria ${subtotal}`);

console.log(`El descuento seria ${descuento}`);

console.log(`El total seria ${total}`);
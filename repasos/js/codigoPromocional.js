// Elabore un algoritmos que dependiendo del codigo promocional realice el descuento a una factura.
// Los codigos promocionales son:
// 2023 y tiene un descuento del 23%,
// 2021 y tiene un descuento del 21%,
// 2022 y tiene un descuento del 22%,
// 1950 y tiene un descuento del 50%
// Debe tener en cuenta que la factura se hace para un solo producto y la cantidad minima del producto son 2 si se quiere aplicar el descuento.

const nombreProducto = prompt("Digite el nombre del producto")
const precioProducto = parseInt(prompt("Digite el precio del producto"))
const cantidadProducto = parseInt(prompt("Digite la cantidad del producto"))
const codigoPromocional = prompt("Digite el codigo promocional")

const subtotal = precioProducto * cantidadProducto

let porcentaje = 0
let descuento = 0

if (codigoPromocional === '2023') {
    porcentaje = 0.23
} else if (codigoPromocional === '2021') {
    porcentaje = 0.21
} else if (codigoPromocional === '2022') {
    porcentaje = 0.22
} else if (codigoPromocional === '1950') {
    porcentaje = 0.50
}

if (cantidadProducto >= 2) {
    descuento = subtotal * porcentaje
} else {
    descuento = 0
}

total = subtotal - descuento

console.log(`El producto ${nombreProducto} tiene un valor de ${precioProducto} y se compro ${cantidadProducto} cantidad`);
console.log(`El subtotal es ${subtotal}`);
console.log(`El descuento es ${descuento}`);
console.log(`El total es ${total}`);
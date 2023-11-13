// Realizar una factura con un descuento que depende del sexo de una persona. Si es mujer el descuento es del 12% y si es hombre el descuento es del 15%, la factura tiene 1 producto y si la cantidad del producto es mayor a 5 el descuento seria el doble.

const sexoPersona = prompt("Digite el sexo de la persona")
const nombreProducto = prompt("Digite el nombre del producto")
const cantidadProducto = parseInt(prompt("Digite el cantidad del prodcuto"))
const precioProducto = parseInt(prompt("Digite el precio del prodcuto"))

const subtotal = cantidadProducto * precioProducto

let porcentajeDescuento = 0

if (sexoPersona === "hombre") {
    porcentajeDescuento = 0.15
} else if (sexoPersona === "mujer") {
    porcentajeDescuento = 0.12
}

if (cantidadProducto > 5) {
    porcentajeDescuento = porcentajeDescuento * 2
}

const descuento = subtotal * porcentajeDescuento
const neto = subtotal - descuento

console.log(`El subtotal es ${subtotal}`);
console.log(`El porcentaje es ${porcentajeDescuento}`);
console.log(`El descuento es ${descuento}`);
console.log(`El neto es ${neto}`);
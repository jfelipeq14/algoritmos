// Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

let compra = parseInt(prompt("Ingrese el total de la compra"));
let descuento = compra * 0.15;
let totalPagar = compra - descuento;

alert(`El total a pagar es: ${totalPagar}`);
// Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

const sueldoBase = parseInt(prompt("Ingrese el sueldo base"));

const venta1 = parseInt(prompt("Ingrese el valor de la primera venta")) * 0.10;
const venta2 = parseInt(prompt("Ingrese el valor de la segunda venta")) * 0.10;
const venta3 = parseInt(prompt("Ingrese el valor de la tercera venta")) * 0.10;

const comision = venta1 + venta2 + venta3;

const total = sueldoBase + comision;

console.log(`El total a recibir es: ${total}`);
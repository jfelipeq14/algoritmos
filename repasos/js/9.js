// 9) Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica
// de refacciones. La empresa, dependiendo del monto total de la compra, decidirá qué hacer
// para pagar al fabricante. Si el monto total de la compra excede de $500 000 la empresa
// tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir
// prestado al banco un 30% y el resto lo pagara solicitando un crédito al fabricante. Si el
// monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir
// de su propio dinero un 70% y el restante 30% lo pagara solicitando crédito al fabricante. El
// fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a
// crédito. 

const numeroPiezas = parseInt(prompt("Digite la cantidad de piezas a comprar"))
const precioPiezas = parseInt(prompt("Digite el precio de la pieza"))

const montoTotal = numeroPiezas * precioPiezas

let dineroPropio = 0
let dineroBanco = 0
let dineroFabricante = 0

if (montoTotal > 500000) {
    dineroPropio = montoTotal * 0.55
    dineroBanco = montoTotal * 0.30
    dineroFabricante = montoTotal * 0.15
} else if (montoTotal <= 500000) {
    dineroPropio = montoTotal * 0.70
    dineroFabricante = montoTotal * 0.30
}
const interesCredito = dineroFabricante * 0.20
const creditoFabricante = dineroFabricante + interesCredito

console.log(`Dinero propio ${dineroPropio}`);
console.log(`Dinero banco ${dineroBanco}`);
console.log(`Dinero fabricante ${dineroFabricante}`);
console.log(`Dinero de interes ${interesCredito}`);
console.log(`Dinero credito ${creditoFabricante}`);


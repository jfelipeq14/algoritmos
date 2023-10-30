// Escriba un programa que pregunte al usuario el valor de un producto y, en función de su valorproducto, le aplique el siguiente descuento:

//Si el valorproducto es inferior a 10 euros, el descuento es del 10%.
//Si el valorproducto es igual o superior a 10 euros y menor que 100 euros, el descuento es del 5%.
//Si el valorproducto es igual o superior a 100 euros, el descuento es del 2%.

// Analisis:
// Entrada => ValorProducto
// Proceso => Validacion para los descuentos
// Salida => Descuento y Total a pagar

const valorProducto = parseInt(prompt("ingrese el valor del producto"))

if (valorProducto < 10) {

    const descuento = valorProducto * 0.10
    const total = valorProducto - descuento
    alert(`El total a pagar es ${total} por el descuento del 10% (${descuento})`)

} else if (valorProducto => 10 && valorProducto < 100) {
    const descuento = valorProducto * 0.05
    const total = valorProducto - descuento
    alert(`El total a pagar es ${total} por el descuento del 5% (${descuento})`)

} else if (valorProducto => 100) {
    const descuento = valorProducto * 0.02
    const total = valorProducto - descuento
    alert(`El total a pagar es ${total} por el descuento del 2% (${descuento})`)
}

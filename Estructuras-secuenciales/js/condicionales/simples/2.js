// Pedir al usuario un número. Si el número es par, imprimir "El número es par". Si no, imprimir "El número es impar".

// entradas
// Numero
// proceso
// Validar si es par o impar (modulo de 2)
//salida
//mensaje de par o impar

const numero = parseInt(prompt("Digite el numero"))

if (numero % 2 == 0) {
    alert(`El numero ${numero} es par`)
} else {
    alert(`El numero ${numero} es impar`)
}
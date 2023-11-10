// Cuantos empleados son solteros, casados, separados, unión libre, divorciados y viudos tiene una empresa y sabemos que el numero total de empleados es 10. 

let solteros = 0
let acumSolteros = ""
let casados = 0
let separados = 0
let unionLibre = 0
let divorciados = 0
let viudos = 0

let empleado1 = prompt("Digite el estado civil del empleado 1")
if (empleado1 === "soltero") {
    solteros = solteros + 1 //suma en x cantidad
    acumSolteros = acumSolteros + empleado1 //acumula las variables
} else if (empleado1 === "casado") {
    casados = casados + 1
} else if (empleado1 === "separado") {
    separados = separados + 1
} else if (empleado1 === "union libre") {
    unionLibre = unionLibre + 1
} else if (empleado1 === "divorciado") {
    divorciados = divorciados + 1
} else if (empleado1 === "viudo") {
    viudos = viudos + 1
}
let empleado2 = prompt("Digite el estado civil del empleado 2")
if (empleado2 === "soltero") {
    solteros = solteros + 1 //contador
    acumSolteros = acumSolteros + empleado2 //acumulador
} else if (empleado2 === "casado") {
    casados = casados + 1
} else if (empleado2 === "separado") {
    separados = separados + 1
} else if (empleado2 === "union libre") {
    unionLibre = unionLibre + 1
} else if (empleado2 === "divorciado") {
    divorciados = divorciados + 1
} else if (empleado2 === "viudo") {
    viudos = viudos + 1
}
let empleado3 = prompt("Digite el estado civil del empleado 3")
if (empleado3 === "soltero") {
    solteros = solteros + 1 //contador
    acumSolteros = acumSolteros + empleado3 //acumulador
} else if (empleado3 === "casado") {
    casados = casados + 1
} else if (empleado3 === "separado") {
    separados = separados + 1
} else if (empleado3 === "union libre") {
    unionLibre = unionLibre + 1
} else if (empleado3 === "divorciado") {
    divorciados = divorciados + 1
} else if (empleado3 === "viudo") {
    viudos = viudos + 1
}
let empleado4 = prompt("Digite el estado civil del empleado 4")
if (empleado4 === "soltero") {
    solteros = solteros + 1
} else if (empleado4 === "casado") {
    casados = casados + 1
} else if (empleado4 === "separado") {
    separados = separados + 1
} else if (empleado4 === "union libre") {
    unionLibre = unionLibre + 1
} else if (empleado4 === "divorciado") {
    divorciados = divorciados + 1
} else if (empleado4 === "viudo") {
    viudos = viudos + 1
}
let empleado5 = prompt("Digite el estado civil del empleado 5")
if (empleado5 === "soltero") {
    solteros = solteros + 1
} else if (empleado5 === "casado") {
    casados = casados + 1
} else if (empleado5 === "separado") {
    separados = separados + 1
} else if (empleado5 === "union libre") {
    unionLibre = unionLibre + 1
} else if (empleado5 === "divorciado") {
    divorciados = divorciados + 1
} else if (empleado5 === "viudo") {
    viudos = viudos + 1
}

alert("solteros " + solteros)
alert("casados " + casados)
alert("separados " + separados)
alert("unionLibre " + unionLibre)
alert("divorciados " + divorciados)
alert("viudos " + viudos)
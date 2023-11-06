// El Sena lo contrata para que elabore un algoritmo que muestre la nota promedio de una ficha sabiendo que hay 4 aprendices y cada aprendiz tiene 3 competencia y cada competencia tiene 2 notas. Si la nota promedio de la ficha es mayor a 3.5 que diga la ficha aprobó. Si es 3.5 que diga la ficha debe reforzar temas y si es inferior a 3,5 que diga la ficha no aprobó el trimestre.

// DE:
// aprendiz1,
// competencia1aprendiz1, nota1competencia1aprendiz1, nota2competencia1aprendiz1
// competencia2aprendiz1, nota1competencia2aprendiz1, nota2competencia2aprendiz1
// competencia3aprendiz1, nota1competencia3aprendiz1, nota2competencia3aprendiz1
// aprendiz2,
// competencia1aprendiz2, nota1competencia1aprendiz2, nota2competencia1aprendiz2
// competencia2aprendiz2, nota1competencia2aprendiz2, nota2competencia2aprendiz2
// competencia3aprendiz2, nota1competencia3aprendiz2, nota2competencia3aprendiz2
// aprendiz3,
// competencia1aprendiz3, nota1competencia1aprendiz3, nota2competencia1aprendiz3
// competencia2aprendiz3, nota1competencia2aprendiz3, nota2competencia2aprendiz3
// competencia3aprendiz3, nota1competencia3aprendiz3, nota2competencia3aprendiz3
// aprendiz4,
// competencia1aprendiz4, nota1competencia1aprendiz4, nota2competencia1aprendiz4
// competencia2aprendiz4, nota1competencia2aprendiz4, nota2competencia2aprendiz4
// competencia3aprendiz4, nota1competencia3aprendiz4, nota2competencia3aprendiz4

// P:
// promediocompetencia1aprendiz1 = (nota1competencia1aprendiz1 + nota2competencia1aprendiz1) / 2
// promediocompetencia2aprendiz1 = (nota1competencia2aprendiz1 + nota2competencia2aprendiz1) / 2
// promediocompetencia3aprendiz1 = (nota1competencia3aprendiz1 + nota2competencia3aprendiz1) / 2
// promedioaprendiz1 = promediocompetencia1aprendiz1 + promediocompetencia2aprendiz1 + promediocompetencia3aprendiz1

// promediocompetencia1aprendiz2 = (nota1competencia1aprendiz2 + nota2competencia1aprendiz2) / 2
// promediocompetencia2aprendiz2 = (nota1competencia2aprendiz2 + nota2competencia2aprendiz2) / 2
// promediocompetencia3aprendiz2 = (nota1competencia3aprendiz2 + nota2competencia3aprendiz2) / 2
// promedioaprendiz2 = promediocompetencia1aprendiz2 + promediocompetencia2aprendiz2 + promediocompetencia3aprendiz2

// promediocompetencia1aprendiz3 = (nota1competencia1aprendiz3 + nota2competencia1aprendiz3) / 2
// promediocompetencia2aprendiz3 = (nota1competencia2aprendiz3 + nota2competencia2aprendiz3) / 2
// promediocompetencia3aprendiz3 = (nota1competencia3aprendiz3 + nota2competencia3aprendiz3) / 2
// promedioaprendiz3 = promediocompetencia1aprendiz3 + promediocompetencia2aprendiz3 + promediocompetencia3aprendiz3

// promediocompetencia1aprendiz4 = (nota1competencia1aprendiz4 + nota2competencia1aprendiz4) / 2
// promediocompetencia2aprendiz4 = (nota1competencia2aprendiz4 + nota2competencia2aprendiz4) / 2
// promediocompetencia3aprendiz4 = (nota1competencia3aprendiz4 + nota2competencia3aprendiz4) / 2
// promedioaprendiz4 = promediocompetencia1aprendiz4 + promediocompetencia2aprendiz4 + promediocompetencia3aprendiz4

// promedioFicha = (promedioaprendiz1 + promedioaprendiz2 + promedioaprendiz3 + promedioaprendiz4) / 4

// si (promedioFicha < 3.5) => message = la ficha no aprobó el trimestre
//  sino
//   si (promedioFicha == 3.5) => message = la ficha debe reforzar temas
//  sino
//   si (promedioFicha > 3.5) => message = la ficha aprobó.

// DS: promedioFicha, message
let message = ""
let aprendiz1 = prompt("Digite el nombre del aprendiz")
let competencia1aprendiz1 = prompt("Digite el nombre de la competencia 1")
let nota1competencia1aprendiz1 = parseFloat(prompt("Digite la nota 1 de la competencia 1"))
let nota2competencia1aprendiz1 = parseFloat(prompt("Digite la nota 2 de la competencia 1"))
let promediocompetencia1aprendiz1 = (nota1competencia1aprendiz1 + nota2competencia1aprendiz1) / 2

let competencia2aprendiz1 = prompt("Digite el nombre de la competencia 2")
let nota1competencia2aprendiz1 = parseFloat(prompt("Digite la nota 1 de la competencia 2"))
let nota2competencia2aprendiz1 = parseFloat(prompt("Digite la nota 2 de la competencia 2"))
let promediocompetencia2aprendiz1 = (nota1competencia2aprendiz1 + nota2competencia2aprendiz1) / 2

let competencia3aprendiz1 = prompt("Digite el nombre de la competencia 3")
let nota1competencia3aprendiz1 = parseFloat(prompt("Digite la nota 1 de la competencia 3"))
let nota2competencia3aprendiz1 = parseFloat(prompt("Digite la nota 2 de la competencia 3"))
let promediocompetencia3aprendiz1 = (nota1competencia3aprendiz1 + nota2competencia3aprendiz1) / 2

let promedioaprendiz1 = (promediocompetencia1aprendiz1 + promediocompetencia2aprendiz1 + promediocompetencia3aprendiz1) / 3

let aprendiz2 = prompt("Digite el nombre del aprendiz")
let competencia1aprendiz2 = prompt("Digite el nombre de la competencia 1")
let nota1competencia1aprendiz2 = parseFloat(prompt("Digite la nota 1 de la competencia 1"))
let nota2competencia1aprendiz2 = parseFloat(prompt("Digite la nota 2 de la competencia 1"))
let promediocompetencia1aprendiz2 = (nota1competencia1aprendiz2 + nota2competencia1aprendiz2) / 2

let competencia2aprendiz2 = prompt("Digite el nombre de la competencia 2")
let nota1competencia2aprendiz2 = parseFloat(prompt("Digite la nota 1 de la competencia 2"))
let nota2competencia2aprendiz2 = parseFloat(prompt("Digite la nota 2 de la competencia 2"))
let promediocompetencia2aprendiz2 = (nota1competencia2aprendiz2 + nota2competencia2aprendiz2) / 2

let competencia3aprendiz2 = prompt("Digite el nombre de la competencia 3")
let nota1competencia3aprendiz2 = parseFloat(prompt("Digite la nota 1 de la competencia 3"))
let nota2competencia3aprendiz2 = parseFloat(prompt("Digite la nota 2 de la competencia 3"))
let promediocompetencia3aprendiz2 = (nota1competencia3aprendiz2 + nota2competencia3aprendiz2) / 2
let promedioaprendiz2 = (promediocompetencia1aprendiz2 + promediocompetencia2aprendiz2 + promediocompetencia3aprendiz2) / 3

let aprendiz3 = prompt("Digite el nombre del aprendiz")
let competencia1aprendiz3 = prompt("Digite el nombre de la competencia 1")
let nota1competencia1aprendiz3 = parseFloat(prompt("Digite la nota 1 de la competencia 1"))
let nota2competencia1aprendiz3 = parseFloat(prompt("Digite la nota 2 de la competencia 1"))
let promediocompetencia1aprendiz3 = (nota1competencia1aprendiz3 + nota2competencia1aprendiz3) / 2

let competencia2aprendiz3 = prompt("Digite el nombre de la competencia 2")
let nota1competencia2aprendiz3 = parseFloat(prompt("Digite la nota 1 de la competencia 2"))
let nota2competencia2aprendiz3 = parseFloat(prompt("Digite la nota 2 de la competencia 2"))
let promediocompetencia2aprendiz3 = (nota1competencia2aprendiz3 + nota2competencia2aprendiz3) / 2

let competencia3aprendiz3 = prompt("Digite el nombre de la competencia 3")
let nota1competencia3aprendiz3 = parseFloat(prompt("Digite la nota 1 de la competencia 3"))
let nota2competencia3aprendiz3 = parseFloat(prompt("Digite la nota 2 de la competencia 3"))
let promediocompetencia3aprendiz3 = (nota1competencia3aprendiz3 + nota2competencia3aprendiz3) / 2
let promedioaprendiz3 = (promediocompetencia1aprendiz3 + promediocompetencia2aprendiz3 + promediocompetencia3aprendiz3) / 3

let aprendiz4 = prompt("Digite el nombre del aprendiz")
let competencia1aprendiz4 = prompt("Digite el nombre de la competencia 1")
let nota1competencia1aprendiz4 = parseFloat(prompt("Digite la nota 1 de la competencia 1"))
let nota2competencia1aprendiz4 = parseFloat(prompt("Digite la nota 2 de la competencia 1"))
let promediocompetencia1aprendiz4 = (nota1competencia1aprendiz4 + nota2competencia1aprendiz4) / 2

let competencia2aprendiz4 = prompt("Digite el nombre de la competencia 2")
let nota1competencia2aprendiz4 = parseFloat(prompt("Digite la nota 1 de la competencia 2"))
let nota2competencia2aprendiz4 = parseFloat(prompt("Digite la nota 2 de la competencia 2"))
let promediocompetencia2aprendiz4 = (nota1competencia2aprendiz4 + nota2competencia2aprendiz4) / 2

let competencia3aprendiz4 = prompt("Digite el nombre de la competencia 3")
let nota1competencia3aprendiz4 = parseFloat(prompt("Digite la nota 1 de la competencia 3"))
let nota2competencia3aprendiz4 = parseFloat(prompt("Digite la nota 2 de la competencia 3"))
let promediocompetencia3aprendiz4 = (nota1competencia3aprendiz4 + nota2competencia3aprendiz4) / 2
let promedioaprendiz4 = (promediocompetencia1aprendiz4 + promediocompetencia2aprendiz4 + promediocompetencia3aprendiz4) / 3

let promedioFicha = (promedioaprendiz1 + promedioaprendiz2 + promedioaprendiz3 + promedioaprendiz4) / 4

if (promedioFicha < 3.5) {
    message = "la ficha no aprobó el trimestre"
} else if (promedioFicha == 3.5) {
    message = "la ficha debe reforzar temas"
} else if (promedioFicha > 3.5) {
    message = "la ficha aprobo"
}

alert(promedioFicha)
alert(message)
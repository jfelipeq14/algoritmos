let e1, e2, e3, e4, e5, e6, e7, e8, e9, e10

e1 = parseInt(prompt("Ingrese la edad 1: "));
e2 = parseInt(prompt("Ingrese la edad 2: "));
e3 = parseInt(prompt("Ingrese la edad 3: "));
e4 = parseInt(prompt("Ingrese la edad 4: "));
e5 = parseInt(prompt("Ingrese la edad 5: "));
e6 = parseInt(prompt("Ingrese la edad 6: "));
e7 = parseInt(prompt("Ingrese la edad 7: "));
e7 = parseInt(prompt("Ingrese la edad 8: ")); // Error: e7 se lee 2 veces
e9 = parseInt(prompt("Ingrese la edad 9: "));
e10 = parseInt(prompt("Ingrese la edad 10: "));

let suma = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9 + e10;
let promedio = suma / 10; //4.8 or NaN

alert(`El promedio de las 10 edades es: ${promedio}`);
// Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera.

const tiempoLunes = parseFloat(prompt("Ingrese el tiempo del lunes"));
const tiempoMiercoles = parseFloat(prompt("Ingrese el tiempo del miércoles"));
const tiempoViernes = parseFloat(prompt("Ingrese el tiempo del viernes"));
const tiempoPromedio = (tiempoLunes + tiempoMiercoles + tiempoViernes) / 3;

alert(`El tiempo promedio es ${tiempoPromedio}`);
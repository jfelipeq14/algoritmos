// El dueño de una tienda compra un artículo a un precio determinado. Obtener el precio en que lo debe vender para obtener una ganancia del 30%.

const precioCompra = parseFloat(prompt("Ingrese el precio de compra del artículo"));
const ganancia = precioCompra * 0.30;
const precioVenta = precioCompra + ganancia;

alert(`El precio de compra es: ${precioCompra} y la ganancia es de ${ganancia} para un total de ${precioVenta}`);
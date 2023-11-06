// Elabore un algoritmo que muestre un solo dato. (Valor comisiones osea la suma de todos los 3vendedores)
// La empresa tiene 3 vendedores y cada vendedor tiene 5 clientes y por cada cliente se hace una factura y cada factura tiene 4 productos. El final de cada factura hay un IVA y un descuento. Las comisiones se basan en el valor neto de la factura.

// Si el numero de hijos es cero tiene una comisión de 10% sobre el valor de la factura.
// Si el número de hijos es uno tiene una comisión del 12% sobre el valor de la factura.
// Si el numero de hijos es dos tiene una comisión del 22% sobre el valor de la factura.
// Si el número de hijos es de tres tiene una comisión del 33% sobre el valor de la factura.
// Si el numero de hijos es mas de tres tiene una comisión del 40% sobre el valor de la factura.

// DE:

// nombreV1 = Juan Felipe

// cliente1Vendedor1 = 123456789, cliente2Vendedor1, cliente3Vendedor1, cliente4Vendedor1, cliente5Vendedor1

// nombreProducto1FacturaCliente1 = leche, valorProducto1FacturaCliente1 = 2300, cantidadProducto1FacturaCliente1 = 1
// nombreProducto2FacturaCliente1, valorProducto2FacturaCliente1, cantidadProducto2FacturaCliente1
// nombreProducto3FacturaCliente1, valorProducto3FacturaCliente1, cantidadProducto3FacturaCliente1
// nombreProducto4FacturaCliente1, valorProducto4FacturaCliente1, cantidadProducto4FacturaCliente1.

// iva (19%), descuento (5%)

// cantidadHijosV1 = 0

//P:
// totalProducto1Cliente1 = valorProducto1FacturaCliente1 * cantidadProducto1FacturaCliente1
// totalProducto2Cliente1= valorProducto2FacturaCliente1 * cantidadProducto2FacturaCliente1
// totalProducto3Cliente1 = valorProducto3FacturaCliente1 * cantidadProducto3FacturaCliente1
// totalProducto4Cliente1= valorProducto4FacturaCliente1 * cantidadProducto4FacturaCliente1
// facturaCliente1Vendedor1 = totalProducto1Cliente1 + totalProducto2Cliente1 + totalProducto3Cliente1 + totalProducto4Cliente1

// ivaTotal = facturaCliente1Vendedor1 * iva
// facturaCliente1Vendedor1 = facturaCliente1Vendedor1 + ivaTotal
// descuentoTotal = facturaCliente1Vendedor1 * descuento
// facturaCliente1Vendedor1 = facturaCliente1Vendedor1 + descuentoTotal

// si (cantidadHijosV1 = 0) => comision = 0.10
//  sino
//   si (cantidadHijosV1 = 1) => comision = 0.12
//  sino
//   si (cantidadHijosV1 = 2) => comision = 0.22
//  sino
//   si (cantidadHijosV1 = 3) => comision = 0.33
//  sino
//   si (cantidadHijosV1 > 3) => comision = 0.40
// totalComisionC1V1 =  facturaCliente1Vendedor1 * comision

// totalComisionC2V1 =  facturaCliente2Vendedor1 * comision
// totalComisionC3V1 =  facturaCliente3Vendedor1 * comision
// totalComisionC4V1 =  facturaCliente4Vendedor1 * comision
// totalComisionC5V1 =  facturaCliente5Vendedor1 * comision

// totalComisionV1 = totalComisionC1V1 + totalComisionC2V1 + totalComisionC3V1 + totalComisionC4V1 + totalComisionC5V1

// DS: totalComisionV1 + totalComisionV2 + totalComisionV3
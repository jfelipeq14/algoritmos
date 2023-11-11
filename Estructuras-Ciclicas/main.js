const facturas = []

function obtenerFacturas() {
    facturasService.getAll().suscribe(
        (data) => {
            if (data) {
                facturas.push(data)
            } else {
                alert("No hay facturas para mostrar")
            }
        }
    )
}



function buscarFacturaPorId(id) {
    const idProductoFactura = facturas.find(x => x.id = id)
    if (idProductoFactura) {
        console.log("Si lo encontre", idProductoFactura.nombre);
    } else {
        console.log("No hay facturas con ese id");
    }
}
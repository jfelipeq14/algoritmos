(() => {

    let nombreDeVariable; //declaracion de variable
    let nombreDeVariable2 = 1; //Inicializacion de variable

    // let se utiliza para declarar variables que pueden ser reasignadas a un nuevo valor. Por ejemplo:
    let x = 1;
    x = 2; // se puede reasignar

    // const se utiliza para declarar variables que no pueden ser reasignadas a un nuevo valor. Por ejemplo:
    const y = 1;
    y = 2; // esto dará un error


    // cadena de texto
    let nombreDePersona = "Juan Felipe";
    console.log(nombreDePersona);

    // numero
    let edadDePersona = 22;
    console.log(edadDePersona);

    // booleano
    let autenticado = false;
    console.log(autenticado);

    // arreglo
    const edadPersonas = [22, 19, 18, 22, 20];
    console.log(edadPersonas);
    console.log(edadPersonas[0]);
    console.log(edadPersonas[1]);

    // objeto
    const objetoPersona = {
        nombre: "Juan Felipe",
        edad: 22,
        estadoSalud: true,
    }
    console.log(objetoPersona);


    // arreglo de objetos
    const informacionDePersonas = [{
        nombre: "Juan Felipe",
        edad: 22,
        estadoSalud: true,
    }, {
        nombre: "Sebastian",
        edad: 19,
        estadoSalud: true,
    }]
    console.log(informacionDePersonas);

    // operadores:
    // variable < 1 (menor a 1)
    // variable > 0 (mayor a 0)
    // varaible <= 1 (menor o igual a 1)
    // variable >= 0 (mayor o igual a 0)
    // variable == 0 (es igual en valor a 0)
    // variable === 0 (es igual en valor y tipo a 0)
    // variable != 0 (es diferente en valor a 0)
    // variable !== 0 (es diferente en valor y tipo a 0)
})()
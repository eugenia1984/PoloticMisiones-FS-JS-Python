//Agrego un addEventListeenr al document y paso como parámetros el DOMContentLoader y una funcion
document.addEventListener("DOMContentLoaded", function(){
  //Accedo al DOM guardando mis elementos del HTML en variables
  const calculadora = document.querySelector(".calculadora")
  const botones = calculadora.querySelector(".calculadora__botones")
  const display = document.querySelector('.calculadora__display')
  //Uso el método .addEventListener y le paso el atributo ONCLICK y otro segundo atributo que es una ARROW FUNCTION
  botones.addEventListener('click', e => {
     // e es el evento que dispara, al que voy a hacer target, para ver si hay un match de que sea un botón, si no lo es lo ignora
      if (e.target.matches('button')) {
      
          const tecla = e.target
          //accedo a la tecla para ver que el evento de hacer click sea en un boton y la guardo en una varaible que nombro tecla y es constante
          const accion = tecla.dataset.accion
          //accedo a la accion de la tecla mediante el data-set
          const contenidoDelBoton = tecla.textContent
          //Trabajo con lo que tengo en el boton
          const numeroMostrado = display.textContent
          //lo que ve se en el display
          const teclaTipeadaAnteriormente = calculadora.dataset.teclaTipeadaAnteriormente
          
          if (!accion) { 
            //niego la accion, ac va a ser un numero que no tiene data-accion
              console.log('boton de numero!')  
              //Para que en el display me muestre los numeros que voy haciendo click  
              if(numeroMostrado === '0' || teclaTipeadaAnteriormente === 'operador' ){
                      display.textContent =   contenidoDelBoton            
              }else{
                display.textContent =  numeroMostrado + contenidoDelBoton
              }
              calculadora.dataset.teclaTipeadaAnteriormente = 'numero'
          }
          if (accion === 'sumar' ||
              accion === 'restar' ||
              accion === 'multiplicar' ||
              accion === 'dividir') {
              console.log('boton de operacion!'); 
              //Seteo estados
              calculadora.dataset.teclaTipeadaAnteriormente = 'operador'
              calculadora.dataset.primerValor = numeroMostrado
              calculadora.dataset.operador = accion
          }
          if (accion === 'decimal') {
              console.log('boton decimal!');
              display.textContent = numeroMostrado + '.'
              calculadora.dataset.teclaTipeadaAnteriormente = 'decimal'
          }

          if (accion === 'borrar') {
              console.log('boton de borrar!');
              display.textContent = 0
              //Para des setear que quede el mismo numero y ultimo operador seteado, para que no se repita la ultima operacion
              calculadora.dataset.teclaTipeadaAnteriormente = ''
              calculadora.dataset.primerValor = ''
              calculadora.dataset.operador = ''
          }

          if (accion === 'calcular') {
              console.log('boton de igual!');
              display.textContent = calcular(calculadora.dataset.primerValor, calculadora.dataset.operador, numeroMostrado);
          }
      }
  });

});

//Creo la funcion calcular() que recibe como parametros dos numeros y el operador para hacer el calculo
function calcular(n1, operador, n2){
let resultado = '' //variable auxiliar en la que guardo el resultado
if(operador === 'sumar'){
  resultado = parseFloat(n1) + parseFloat(n2);
} else if(operador === 'restar'){
  resultado = parseFloat(n1) - parseFloat(n2);
} else if(operador === 'multiplicar'){
  resultado = parseFloat(n1) * parseFloat(n2);
} else if(operador === 'dividir'){
  resultado = parseFloat(n1) / parseFloat(n2);
}
  return resultado;
}






  





//Agrego un addEventListeenr al document y paso como parámetros el DOMContentLoader y una funcion
document.addEventListener('DOMContentLoader', function() {
  //Accedo al DOM guardando mis elementos del HTML en variables
  const calculadora = document.querySelector(".calculadora")
  const botones = calculadora.querySelector(".calculadora__botones")
  const display = document.querySelector(".calculadora__display")
  //Uso el método .addEventListener y le paso el atributo ONCLICK y otro segundo atributo que es una ARROW FUNCTION
  botones.addEventListener('click', e => {
    // e es el evento que dispara, al que voy a hacer target, para ver si hay un match de que sea un botón, si no lo es lo ignora
    if (e.target.matches('button')) {
      const tecla = e.target //accedo a la tecla para ver que el evento de hacer click sea en un boton y la guardo en una varaible que nombro tecla y es constante
      const accion = tecla.dataset.action //accedo a la accion de la tecla mediante el data-set
      if (!accion) { //niego la accion, ac va a ser un numero que no tiene data-accion
        console.log("Botón de número")
      }
      if (accion == 'sumar' || 
          accion == 'restar' || 
          accion == 'multiplicar' || 
          accion == 'dividir') {
          console.log("operacion");
      }
      if (accion =='decimal') {
          console.log('boton decimal');
      }
      if (accion =='borrar') {
          console.log('boton de borrar');
      }
      if (accion =='calcular') {
          console.log('boton de igual');
      }
    }
  });
});
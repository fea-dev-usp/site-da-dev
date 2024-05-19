function aumentaZoom() {
  var elementosTexto = document.querySelectorAll('body *');
  for (let c = 0; c < elementosTexto.length; c++) {
    const elemento = elementosTexto[c];
    const fontSize = parseInt(window.getComputedStyle(elemento)['font-size']);
    elemento.style.fontSize = (fontSize + 1) + 'px';
  }
}

function diminuiZoom() {
  var elementosTexto = document.querySelectorAll('body *');
  for (let c = 0; c < elementosTexto.length; c++) {
    const elemento = elementosTexto[c];
    const fontSize = parseInt(window.getComputedStyle(elemento)['font-size']);
    elemento.style.fontSize = (fontSize - 1) + 'px';
  }
}

function resetZoom() {
  var elementosTexto = document.querySelectorAll('body *');
  for (let c = 0; c < elementosTexto.length; c++) {
    const elemento = elementosTexto[c];
    elemento.style.fontSize = '';
  }
}


function alternarTema() {
  var tema = document.querySelector("html").getAttribute("data-bs-theme");
  if (tema === "light") {
    document.querySelector("html").setAttribute("data-bs-theme", "dark");
  } else {
    document.querySelector("html").setAttribute("data-bs-theme", "light");
  }
}

document.querySelector("html").setAttribute("data-bs-theme", "dark");




window.onload = function () {
  var botoes = document.querySelectorAll("i");
  for (let i = 0; i < botoes.length; i++) {
    botoes[0].addEventListener("click", aumentaZoom);
    botoes[1].addEventListener("click", diminuiZoom);
    botoes[2].addEventListener("click", resetZoom);
    botoes[3].addEventListener("click", alternarTema);
  }
}

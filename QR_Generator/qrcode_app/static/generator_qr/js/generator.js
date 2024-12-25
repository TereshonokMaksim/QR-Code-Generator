document.querySelector('.input-file').onchange = function () {
    document.querySelector('#text-file').innerHTML = this.value.split('\\').at(-1);
  }

  const colorInput = document.querySelector(".input-color");
  const colorPreview = document.getElementById("color-preview");

  colorInput.addEventListener("input", () => {
    colorPreview.style.backgroundColor = colorInput.value;
  });

  colorPreview.addEventListener("click", () => {
    colorInput.click();
  });

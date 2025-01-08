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

let selectOpened = false
document.querySelector("select").addEventListener("click", () => {
    if (selectOpened) {
      selectOpened = true
      document.querySelector("select").style = "border-radius: 8px 8px 8px 8px;"
    }
    else {
      selectOpened = false
      document.querySelector("select").style = "border-radius: 8px 8px 0px 0px;"
    }
})
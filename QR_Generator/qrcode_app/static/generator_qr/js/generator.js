document.querySelector('.input-file').onchange = function () {
    document.querySelector('#text-file').innerHTML = this.value.split('\\').at(-1);
  }

  const colorInputs = document.querySelectorAll(".input-color");
  const colorPreview = document.querySelectorAll(".custom-color-picker");

  colorInputs.forEach((colorInput) => {colorInput.addEventListener("input", () => {
  document.querySelector(`#colorPreview${colorInput.id[colorInput.id.length - 1]}`).style.backgroundColor = colorInput.value;
  })});

  colorPreview.forEach((colorPreviewDiv) => {colorPreviewDiv.addEventListener("click", () => {
    console.log(`colorInput${colorPreviewDiv.id[colorPreviewDiv.id.length - 1]}`)
    document.querySelector(`#colorInput${colorPreviewDiv.id[colorPreviewDiv.id.length - 1]}`).click();
  })});

let selectOpened = true
document.querySelector("select").addEventListener("click", () => {
    if (!selectOpened) {
      selectOpened = true
      document.querySelector("select").style = "border-radius: 8px 8px 8px 8px;"
    }
    else {
      selectOpened = false
      document.querySelector("select").style = "border-radius: 8px 8px 0px 0px;"
    }
    console.log(selectOpened)
})
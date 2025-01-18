const openModalButton = document.querySelectorAll('.qrcode-download');
const blurElement = document.querySelector('.blur');
const cross = document.querySelector('.cross-image');
const downloadLink = document.querySelector('.download-link');


for (let buttonNumber = 0; buttonNumber < openModalButton.length; buttonNumber++){
    openModalButton[buttonNumber].addEventListener('click', () => {
        blurElement.style.display = 'flex';
        console.log('text');
        let qrcodeValues = document.getElementById(`card-${ openModalButton[buttonNumber].id}`).querySelector('.qrcode-data').value.split(";");
        document.querySelector('.qrcode-modal').src = qrcodeValues[5];
        downloadLink.href = qrcodeValues[5];
        document.querySelector('.qrcode-name').innerHTML = `Name: ${qrcodeValues[0]}`;
        document.querySelector('.qrcode-date').innerHTML = `Date of creation: ${qrcodeValues[6]}`;
        document.querySelector('.qrcode-size').innerHTML = `Size: ${qrcodeValues[1]}`;
        document.querySelector('.color').style.background = qrcodeValues[2];
        document.querySelector('.qrcode-form').innerHTML = `Form: ${qrcodeValues[3]}`;
        document.querySelector('.qrcode-link').innerHTML = `Content: ${qrcodeValues[4]}`;
    });
}
cross.addEventListener('click', () => {
    blurElement.style.display = 'none';
})

document.onkeyup = (key) => {
    if (key.key == "Escape") {
        blurElement.style.display = 'none' ;
    }
}
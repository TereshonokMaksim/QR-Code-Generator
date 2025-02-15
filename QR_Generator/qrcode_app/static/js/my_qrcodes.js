const openModalButton = document.querySelectorAll('.qrcode-download');
const blurElement = document.querySelector('.blur');
const cross = document.querySelector('.cross-image');
const downloadLink = document.querySelector('.download-link');
const sorting = document.querySelector('.sorting')
let sortingTypes = document.querySelector(".sorting-ids").value.split("/")
let nameSorting = sortingTypes[0].split(",")
let dateSorting = sortingTypes[1].split(",")

for (let buttonNumber = 0; buttonNumber < openModalButton.length; buttonNumber++){
    openModalButton[buttonNumber].addEventListener('click', () => {
        blurElement.style.display = 'flex';
        console.log('text');
        let qrcodeValues = document.getElementById(`card-${ openModalButton[buttonNumber].id}`).querySelector('.qrcode-data').value.split(";");
        document.querySelector('.qrcode-modal').src = qrcodeValues[5];
        downloadLink.href = qrcodeValues[5];
        console.log(qrcodeValues)
        if (qrcodeValues[4].length > 400){
            qrcodeValues[4] = qrcodeValues[4].substr(0, 400) + "..."
        }
        if (qrcodeValues[0].length > 100){
            qrcodeValues[0] = qrcodeValues[0].substr(0, 100) + "..."
        }
        document.querySelector('.qrcode-name').innerHTML = `Name: ${qrcodeValues[0]}`;
        document.querySelector('.qrcode-date').innerHTML = `Date of creation: ${qrcodeValues[6]}`;
        document.querySelector('.qrcode-size').innerHTML = `Size: ${qrcodeValues[1]}`;
        document.querySelector('.front-color').style.background = qrcodeValues[2];
        document.querySelector('.back-color').style.background = qrcodeValues[7];
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
console.log(sorting)
sorting.onchange = () => {
    if (sorting.value == document.querySelector("#data-oldest").value){
        for (let id of dateSorting){
            let myQRCodes = document.querySelector(".myqrcodes-cards")
            if (id == dateSorting[0]){
                myQRCodes.prepend(document.querySelector(`#card-${id}`))
            }
            else{
                myQRCodes.insertBefore(document.querySelector(`#card-${id}`), document.querySelector(`#card-${dateSorting[dateSorting.indexOf(id) - 1]}`).nextSibling)
            }
        }
    }
    else if (sorting.value == document.querySelector("#data-newest").value){
        let dateReversed = [...dateSorting]
        dateReversed = dateReversed.reverse()
        for (let id of dateReversed){
            let myQRCodes = document.querySelector(".myqrcodes-cards")
            if (id == dateReversed[0]){
                myQRCodes.prepend(document.querySelector(`#card-${id}`))
            }
            else{
                myQRCodes.insertBefore(document.querySelector(`#card-${id}`), document.querySelector(`#card-${dateReversed[dateReversed.indexOf(id) - 1]}`).nextSibling)
            }
        }
    }else if (sorting.value == document.querySelector("#alphabet-ascending").value){
        // console.log("ascending")
        for (let id of nameSorting){
            console.log(id, nameSorting.indexOf(id))
            let myQRCodes = document.querySelector(".myqrcodes-cards")
            if (id == nameSorting[0]){
                myQRCodes.prepend(document.querySelector(`#card-${id}`))
            }
            else{
                console.log(document.querySelector(`#card-${nameSorting[nameSorting.indexOf(id) - 1]}`), nameSorting.indexOf(id) - 1)
                myQRCodes.insertBefore(document.querySelector(`#card-${id}`), document.querySelector(`#card-${nameSorting[nameSorting.indexOf(id) - 1]}`).nextSibling)
            } 
        }
    }else if (sorting.value == document.querySelector("#alphabet-descending").value){
        let nameReversed = [...nameSorting]
        nameReversed = nameReversed.reverse()
        for (let id of nameReversed){
            console.log(id, nameReversed.indexOf(id))
            let myQRCodes = document.querySelector(".myqrcodes-cards")
            if (id == nameReversed[0])
            {
                    myQRCodes.prepend(document.querySelector(`#card-${id}`))
            }
            else{
                myQRCodes.insertBefore(document.querySelector(`#card-${id}`), document.querySelector(`#card-${nameReversed[nameReversed.indexOf(id) - 1]}`).nextSibling)
            } 
}  
    }
}

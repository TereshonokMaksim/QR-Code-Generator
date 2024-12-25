const openModalButton = document.querySelectorAll('.modal-class')
const blurElement = document.querySelector('.blur')
const cross = document.querySelector('.cross-image')


for (let buttonNumber = 0; buttonNumber < openModalButton.length; buttonNumber++){
    openModalButton[buttonNumber].addEventListener('click', () => {
        blurElement.style.display = 'flex'
        console.log('text')
    });
}
cross.addEventListener('click', () => {
    blurElement.style.display = 'none'
})
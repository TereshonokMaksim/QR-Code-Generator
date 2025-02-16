const openModalButton = document.querySelectorAll('.modal-class');
const blurElement = document.querySelector('.blur');
const cross = document.querySelector('.cross-image');
const standartSub = document.querySelector('#second-card-price')
const proSub = document.querySelector('#third-card-price')
const standartSubBody = document.querySelector('#subscription-card-standart')
const proSubBody = document.querySelector('#subscription-card-pro')
const freeSubBody = document.querySelector('#subscription-card-free')
const freeSubButton = document.querySelector('#first-card-price')
const hiddenSub = document.querySelector('.hidden-subscription').value.split("/")[0]
const hiddenChangeSub = document.querySelector('.hidden-subscription').value.split("/")[1]

for (let buttonNumber = 0; buttonNumber < openModalButton.length; buttonNumber++){
    openModalButton[buttonNumber].addEventListener('click', () => {
        blurElement.style.display = 'flex';
    });
}
cross.addEventListener('click', () => {
    blurElement.style.display = 'none';
})

if (hiddenSub == 'Free'){
    freeSubBody.classList.add("current-subscription")
    standartSubBody.classList.add("avalaible-subscription")
    proSubBody.classList.add("avalaible-subscription")
    freeSubButton.disabled = true
    freeSubButton.textContent = 'You are subscribed'
}else if (hiddenSub == 'Standart'){
    freeSubBody.classList.add("avalaible-subscription")
    standartSubBody.classList.add("current-subscription")
    proSubBody.classList.add("avalaible-subscription")
    standartSub.disabled = true
    standartSub.textContent = 'You are subscribed'
} else if (hiddenSub == 'Pro'){
    freeSubBody.classList.add("avalaible-subscription")
    standartSubBody.classList.add("avalaible-subscription")
    proSubBody.classList.add("current-subscription")
    proSub.disabled = true
    proSub.textContent = 'You are subscribed'
}

if (hiddenChangeSub == "True"){
    blurElement.style.display = 'flex';
}
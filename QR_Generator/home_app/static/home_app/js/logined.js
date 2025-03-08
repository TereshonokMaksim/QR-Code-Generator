const openModalButton = document.querySelectorAll('.modal-class');
const blurElement = document.querySelector('.blur');
const modalInfo = document.querySelector(".modal-info");
const cardInfo = document.querySelector(".subscription-form")
const cross = document.querySelector('.cross-image');
// const standartSub = document.querySelector('#second-card-price')
// const proSub = document.querySelector('#third-card-price')
// const standartSubBody = document.querySelector('#subscription-card-standart')
// const proSubBody = document.querySelector('#subscription-card-pro')
// const freeSubBody = document.querySelector('#subscription-card-free')
// const freeSubButton = document.querySelector('#first-card-price')
const subBodies = document.querySelectorAll('.subscription-card')
const subButtons = document.querySelectorAll('.subscription-price')
const hiddenSub = document.querySelector('.hidden-subscription').value.split("/")[0]
const hiddenChangeSub = document.querySelector('.hidden-subscription').value.split("/")[1]
let prices = []

function getPrice(body){
    let price = body.querySelector(".subscription-cost").innerHTML.split(" ")
    price = price[price.length - 1].split("/")[0]
    if (price.includes("€")){
        price = Number(price.substring(0, price.length - 1))
    }
    else{
        price = 0
    }
    return price
}

subBodies.forEach((body) => {
    prices.push(getPrice(body))
})
const MAX_PRICE = Math.max(...prices)
console.log(prices, MAX_PRICE)
// for (let buttonNumber = 0; buttonNumber < openModalButton.length; buttonNumber++){
//     openModalButton[buttonNumber].addEventListener('click', () => {
//         blurElement.style.display = 'flex';
//     });
// }
cross.addEventListener('click', () => {
    blurElement.classList.add("hidden");
    modalInfo.classList.add("hidden");
    blurElement.classList.add("hidden");
    cardInfo.classList.add("hidden");
})

// if (hiddenSub == 'Free'){
//     freeSubBody.classList.add("current-subscription")
//     standartSubBody.classList.add("avalaible-subscription")
//     proSubBody.classList.add("avalaible-subscription")
//     freeSubButton.disabled = true
//     freeSubButton.textContent = 'You are subscribed'
// }else if (hiddenSub == 'Standart'){
//     freeSubBody.classList.add("avalaible-subscription")
//     standartSubBody.classList.add("current-subscription")
//     proSubBody.classList.add("avalaible-subscription")
//     standartSub.disabled = true
//     standartSub.textContent = 'You are subscribed'
// } else if (hiddenSub == 'Pro'){
//     freeSubBody.classList.add("avalaible-subscription")
//     standartSubBody.classList.add("avalaible-subscription")
//     proSubBody.classList.add("current-subscription")
//     proSub.disabled = true
//     proSub.textContent = 'You are subscribed'
// }
for (let body of subBodies){
    body.classList.add("avalaible-subscription")
    let priceProportion = getPrice(body) / MAX_PRICE
    let parts = [body.querySelector(".subscription-type"), body.querySelector(".subscription-price")]
    if (priceProportion == 1){
        parts.forEach((part) => {part.classList.add("brightest-option")})
    }
    else if (priceProportion > 0.5){
        parts.forEach((part) => {part.classList.add("brighter-option")})
    }
    else if (priceProportion > 0){
        parts.forEach((part) => {part.classList.add("bright-option")})
    }
    let subButton = body.querySelector(".subscription-price") 
    subButton.addEventListener("click", () => {
        blurElement.classList.toggle("hidden");
        cardInfo.classList.toggle("hidden");
        cardInfo.querySelector("button").value = subButton.value
    })
}

const currentCard = document.querySelector(`#subscription-card-${hiddenSub}`)
const currentCardButton = currentCard.querySelector(".subscription-price")
currentCard.classList.remove("avalaible-subscription")
currentCard.classList.add("current-subscription")
currentCardButton.disabled = true
currentCardButton.querySelector("p").textContent = "You are subscribed"


if (hiddenChangeSub == "True"){
    blurElement.classList.toggle("hidden");
    modalInfo.classList.toggle("hidden");
}

const subBodies = document.querySelectorAll('.subscription-card')
const subButtons = document.querySelectorAll('.subscription-price')
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
}
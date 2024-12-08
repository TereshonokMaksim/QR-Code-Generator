async function getLogined() {
    let location = String(parent.document.location).split("/")
    location = [location[0], location[2]].join("//")
    console.log(location)
    let logined = await fetch(`${location}/is_logined`)
    if (logined.ok) {
        logined = await logined.json()
        return logined["logined"]
    }
    else {
        return logined.status
    }
}

let result = getLogined().then((isLogined) => {
    let blocksToDelete = []
    if (isLogined) {
        blocksToDelete = document.querySelectorAll(".not-logined-blocks")
        document.querySelector(".username").innerHTML = `Welcome, ${isLogined}!`
    }
    else {
        blocksToDelete = document.querySelectorAll(".logined-blocks")
    }
    for (let blockNum = 0; blockNum < blocksToDelete.length; blockNum++) {
        document.querySelector("header").removeChild(blocksToDelete[blockNum])
    }
})
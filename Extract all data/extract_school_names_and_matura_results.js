// Run on https://www.almamater.si/lestvicasol-srednjesole-s181

let rows = document.querySelectorAll("tbody tr")

let raw_data = ""

for (let row of rows) {
    let items = row.querySelectorAll("td div")
    let name = items[1].innerText
    let result = items[2].innerText

    raw_data += name + "*" + result + "!"
}

console.log(raw_data)
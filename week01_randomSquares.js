function setup(){
    createCanvas(800, 600)
    background(128)
    drawBoard(10, 10)
}

function drawBoard(rows, cols) {
    rows = parseInt(randomizer(rows))
    cols = parseInt(randomizer(cols))
    rowDivs = divLength(height, rows)
    colDivs = divLength(width, cols)

    for(let i=0; i<rows; i++){
        for(let j=0; j<cols; j++){
            randomizeFill()
            rect(
                rowDivs[i],
                colDivs[j],
                rowDivs[i+1] - rowDivs[i], 
                colDivs[j+1] - colDivs[j]
            )

        }
    }
}

function divLength(length, units) {
    let dividedLength = 0
    let divArr = [dividedLength]
    for(let i=1; i < units; i++){
        dividedLength += parseInt(randomizer(length - dividedLength))
        divArr.push(dividedLength)
    } 
    divArr.push(length)
    return divArr
}

function randomizer(value) {
    return random(value)
}

function randomizeFill() {
    if (random() > 0.5){
        fill(255)
    }
    else {
        fill(0)
    }
}
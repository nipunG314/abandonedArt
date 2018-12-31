function setup(){
    createCanvas(500, 500)
    background(255)
    frameRate(10)
}

function draw(){
    clear()    
    background(255)
    angleMode(DEGREES)
    strokeWeight(3)
    beginShape()

    let centX = width/2, centY = height/2
    let x = 0, y = 0
    let radius = 100

    for(let i = 0; i<360; i++){
        drawRadius = radius * random()
        x = centX + drawRadius*cos(i)
        y = centY + drawRadius*sin(i)
        curveVertex(x, y)
    }

    endShape(CLOSE)
}
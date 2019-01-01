function setup(){
    createCanvas(800, 600)
    background(255)
    strokeWeight(3)

    let centX = width/2
    let centY = height/2
    let radius = 200

    beginShape()
    angleMode(DEGREES)
    for(let i=0; i<720; i++){
        let p = 10.5*i
        let x = centX + radius*cos(p)*cos(i)
        let y = centY + radius*cos(p)*sin(i)

        curveVertex(x, y)
    }
    endShape(CLOSE)
    fill(255)
    ellipse(centX, centY, 50, 50)

}

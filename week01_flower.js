function setup(){
    createCanvas(800, 600)
    background(255)
    strokeWeight(3)

    let centX = width/2
    let centY = height/2
    let radius = 200
    let seed = random()

    beginShape()
    angleMode(DEGREES)
    for(let i=0; i<720; i++){
        let p = 10.5*i
        let x = centX + noise(seed) * radius*cos(p)*cos(i)
        let y = centY + noise(seed) * radius*cos(p)*sin(i)
        seed += 0.0005

        curveVertex(x, y)
    }
    endShape(CLOSE)
    fill(255)
    ellipse(centX, centY, 50, 50)

}

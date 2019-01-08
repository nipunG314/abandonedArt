class LineBoard {
    constructor() {
        this.step = 0
        this.linePartition = {0: 1}
    }

    update(){

    }

    draw(){

    }
}

let canvasRenderer

function centerCanvas(cnv){
    let x = (windowWidth - width) / 2;
    let y = (windowHeight - height) / 2;
    cnv.position(x, y);
}

function setup(){
    let canvasRenderer = createCanvas(800, 600);
    centerCanvas(canvasRenderer)
    background(255)

    noFill()
    beginShape()
    vertex(0, 0)
    vertex(width, 0)
    vertex(width, height)
    vertex(0, height)
    endShape(CLOSE)

    line(0, 300, width, 300)
}



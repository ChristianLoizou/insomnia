function setup() {
    createCanvas(800, 800);
}

function draw() {
    background(51);
    rectMode(CENTER);
    ellipse(mouseX, mouseY, 75, 75, 15);
}
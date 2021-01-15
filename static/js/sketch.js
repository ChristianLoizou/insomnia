const ELLIPSE_SIZE = 25;

var positions;


function setup() {
    createCanvas(800, 800);
    positions = [];
}

function draw() {
    background(51);
    noStroke();
    fill(120);
    positions.forEach(function (vector, index) {
        ellipse(vector.x, vector.y, ELLIPSE_SIZE);
    });
    fill(118, 118, 125);
    ellipse(mouseX, mouseY, ELLIPSE_SIZE);

}

function mousePressed() {
    position = createVector(mouseX, mouseY);
    positions.push(position);
}

function mouseDragged() {
    position = createVector(mouseX, mouseY);
    positions.push(position);
}
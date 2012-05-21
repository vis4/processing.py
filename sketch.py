
from P5 import *


def setup():
    size(400, 400)
    stroke(255)
    background(192, 64, 0)
    noFill()
    smooth()

pts = []


def draw():
    curveTightness(0.03)
    background(192, 64, 0)
    beginShape()
    for x, y in pts:
        curveVertex(x, y)
    endShape()


def mouseDragged(evt):
    if len(pts) > 0:
        x, y = pts[-1]
        d = dist(x, y, mouse.x, mouse.y)
        if d < 30:
            return
    pts.append((mouse.x, mouse.y))

run(globals())

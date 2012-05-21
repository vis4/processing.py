
from P5 import *

smallPoint = 2
top = left = largePoint = 0
img = None


def setup():
    global largePoint, left, top, img
    size(500, 500)
    frameRate(120)
    img = loadImage("../data/melon.jpg")
    noStroke()
    background(255)
    smooth()
    largePoint = min(P5.width, P5.height) / 10
    left = (P5.width - img.width) / 2
    top = (P5.height - img.height) / 2


def draw():
    pointillize = P5.map(mouse.x, 0, P5.width, smallPoint, largePoint)
    x = int(random(img.width))
    y = int(random(img.height))
    pix = img.get(x, y)
    fill(pix, 128)
    ellipse(left + x, top + y, pointillize, pointillize)
    if P5.frameCount % 100 == 0:
        print round(P5.frameRate), 'frames per second'

run(globals())

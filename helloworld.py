
from P5 import *

def setup():
    size(400, 400)
    smooth()

def draw():
    if mouse.pressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouse.x, mouse.y, 80, 80)

run(globals())

# Animator.
# http://processing.org/learning/topics/animator.html

from P5 import *


currentFrame = 0
frames = [PImage() for i in range(24)]
lastTime = 0


def setup():
    size(640, 200)
    strokeWeight(12)
    frameRate(30)
    smooth()
    background(0)
    stroke(240)
    for i in range(len(frames)):
        frames[i] = get()


def draw():
    global lastTime
    currentTime = millis()
    if currentTime > lastTime + 30:
        nextFrame()
        lastTime = currentTime

    if mouse.pressed:
        line(mouse.px, mouse.py, mouse.x, mouse.y)


def nextFrame():
    global currentFrame
    frames[currentFrame] = get()  # Get the display window
    currentFrame += 1  # Increment to next frame
    if currentFrame >= len(frames):
        currentFrame = 0
    image(frames[currentFrame], 0, 0)


run(globals())

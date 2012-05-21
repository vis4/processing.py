processing.py
=============

Allows you to write Processing sketches in Python.


For instance, you can run this ``helloworld.py``

``python
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
``

by calling

``bash
jython helloworld.py
``

### Current progress

Under development. Check example sketches to see what's working already.


### Installation notes

* install Jython
* download core.jar from Processing
* add core.jar to your CLASSPATH


"""
This module wraps global processing.core.PApplet methods inside.
global functions.

Differences to Processing:
- global attributes won't work. Instead you must use the following

    mouse.x
    mouse.y
    mouse.px
    mouse.py
    mouse.pressed
    mouse.btn
    env.frameRate
    env.frameCount

"""

_p9inst = "foo"


def acos(*args): return _p9inst.acos(*args)


## Structure

def exit(*args): _p9inst.exit(*args)
def loop(*args): _p9inst.loop(*args)
def noLoop(*args): _p9inst.noLoop(*args)
def popStyle(*args): _p9inst.popStyle(*args)
def pushStyle(*args): _p9inst.pushStyle(*args)
def size(*args): _p9inst.size(*args)
def redraw(*args): _p9inst.redraw(*args)
def draw(): pass


## Environment

def cursor(*args): _p9inst.cursor(*args)
def frameRate(*args): _p9inst.frameRate(*args)
def noCursor(*args): _p9inst.noCursor(*args)

## Shape

# 2D Primitives
def arc(*args): _p9inst.arc(*args)
def ellipse(*args): _p9inst.ellipse(*args)
def line(*args): _p9inst.line(*args)
def point(*args): _p9inst.point(*args)
def quad(*args): _p9inst.quad(*args)
def rect(*args): _p9inst.rect(*args)
def triangle(*args): _p9inst.triangle(*args)

# Curves
def bezier(*args): _p9inst.bezier(*args)
def bezierDetail(*args): _p9inst.bezierDetail(*args)
def bezierPoint(*args): _p9inst.bezierPoint(*args)
def bezierTangent(*args): _p9inst.bezierTangent(*args)
def curve(*args): _p9inst.curve(*args)
def curveDetail(*args): _p9inst.curveDetail(*args)
def curvePoint(*args): _p9inst.curvePoint(*args)
def curveTangent(*args): _p9inst.curveTangent(*args)
def curveTightness(*args): _p9inst.curveTightness(*args)


# 3D Primitives

# Attributes
def ellipseMode(*args): _p9inst.ellipseMode(*args)
def noSmooth(*args): _p9inst.noSmooth(*args)
def rectMode(*args): _p9inst.rectMode(*args)
def smooth(*args): _p9inst.smooth(*args)
def strokeCap(*args): _p9inst.strokeCap(*args)
def strokeJoin(*args): _p9inst.strokeJoin(*args)
def strokeWeight(*args): _p9inst.strokeWeight(*args)

# Vertex
def beginShape(*args): _p9inst.beginShape(*args)
def bezierVertex(*args): _p9inst.bezierVertex(*args)
def curveVertex(*args): _p9inst.curveVertex(*args)
def endShape(*args): _p9inst.endShape(*args)
def texture(*args): _p9inst.texture(*args)
def textureMode(*args): _p9inst.textureMode(*args)
def vertex(*args): _p9inst.vertex(*args)

# Loading & Displaying

## Color

# Setting
def background(*args): _p9inst.background(*args)
def colorMode(*args): _p9inst.background(*args)
def fill(*args): _p9inst.fill(*args)
def noFill(*args): _p9inst.noFill(*args)
def noStroke(*args): _p9inst.noStroke(*args)
def stroke(*args): _p9inst.stroke(*args)

# Creating & Reading
def alpha(*args): return _p9inst.alpha(*args)
def blendColor(*args): return _p9inst.blendColor(*args)
def blue(*args): return _p9inst.blue(*args)
def brightness(*args): return _p9inst.brightness(*args)
def color(*args): return _p9inst.color(*args)
def green(*args): return _p9inst.green(*args)
def hue(*args): return _p9inst.hue(*args)
def lerpColor(*args): return _p9inst.lerpColor(*args)
def red(*args): return _p9inst.red(*args)
def saturation(*args): return _p9inst.saturation(*args)

def mouseClicked(*args): pass
def mousePressed(*args): pass
def mouseReleased(*args): pass
def mouseMoved(*args): pass
def mouseDragged(*args): pass
def mouseEntered(*args): pass
def mouseExited(*args): pass

## Math

# Operators

# Bitwise Operators

# Calculation
def dist(*args): return _p9inst.dist(*args)


# Random
def noise(*args): return _p9inst.noise(*args)
def noiseDetail(*args): return _p9inst.noiseDetail(*args)
def noiseSeed(*args): return _p9inst.noiseSeed(*args)

# define constants
JAVA2D = 'processing.core.PGraphicsJava2D'


class MouseVars():
    x = None
    y = None
    px = None
    py = None
    btn = 0
    pressed = False

mouse = MouseVars()


class Environment():
    frameRate = None
    frameCount = None

env = Environment()


def p9_set_instance(inst):
    global _p9inst
    _p9inst = inst
    #_p9inst.registerMouseEvent(mouse.mouseEvent)


def p9_update_env():
    env.frameRate = _p9inst.frameRate
    env.frameCount = _p9inst.frameCount


def p9_register_mouse_event(evt):
    if evt.getID() == evt.MOUSE_PRESSED:
        mouse.pressed = True
        mouse.btn = evt.getButton()
    elif evt.getID() == evt.MOUSE_RELEASED:
        mouse.pressed = False

    if evt.getX() != mouse.x or evt.getY() != mouse.y:
        mouse.px = mouse.x
        mouse.py = mouse.y
    mouse.x = evt.getX()
    mouse.y = evt.getY()

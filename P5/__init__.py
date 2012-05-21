
#from sketch import draw, setup, mouseClicked, mousePressed, mouseReleased, mouseMoved, mouseDragged
#from P5 import *

#__all__ = ['run', 'size', 'strokeWeight', 'mouseClicked', 'mousePressed', 'mouseMoved', 'mouseDragged', 'mouseReleased', 'P5_set_instance', 'P5_register_mouse_event']


_P5 = None

from processing.core import PImage  # auto-import PImage

def acos(*args): return _P5.acos(*args)


## Structure

def exit(*args): _P5.exit(*args)
def loop(*args): _P5.loop(*args)
def noLoop(*args): _P5.noLoop(*args)
def popStyle(*args): _P5.popStyle(*args)
def pushStyle(*args): _P5.pushStyle(*args)
def size(*args): _P5.size(*args)
def redraw(*args): _P5.redraw(*args)
def millis(*args): return _P5.millis(*args)
def draw(): pass


## Environment

def cursor(*args): _P5.cursor(*args)
def frameRate(*args): _P5.frameRate(*args)
def noCursor(*args): _P5.noCursor(*args)

## Shape

# 2D Primitives
def arc(*args): _P5.arc(*args)
def ellipse(*args): _P5.ellipse(*args)
def line(*args): _P5.line(*args)
def point(*args): _P5.point(*args)
def quad(*args): _P5.quad(*args)
def rect(*args): _P5.rect(*args)
def triangle(*args): _P5.triangle(*args)

# Curves
def bezier(*args): _P5.bezier(*args)
def bezierDetail(*args): _P5.bezierDetail(*args)
def bezierPoint(*args): _P5.bezierPoint(*args)
def bezierTangent(*args): _P5.bezierTangent(*args)
def curve(*args): _P5.curve(*args)
def curveDetail(*args): _P5.curveDetail(*args)
def curvePoint(*args): _P5.curvePoint(*args)
def curveTangent(*args): _P5.curveTangent(*args)
def curveTightness(*args): _P5.curveTightness(*args)


# 3D Primitives

# Attributes
def ellipseMode(*args): _P5.ellipseMode(*args)
def noSmooth(*args): _P5.noSmooth(*args)
def rectMode(*args): _P5.rectMode(*args)
def smooth(*args): _P5.smooth(*args)
def strokeCap(*args): _P5.strokeCap(*args)
def strokeJoin(*args): _P5.strokeJoin(*args)
def strokeWeight(*args): _P5.strokeWeight(*args)

# Vertex
def beginShape(*args): _P5.beginShape(*args)
def bezierVertex(*args): _P5.bezierVertex(*args)
def curveVertex(*args): _P5.curveVertex(*args)
def endShape(*args): _P5.endShape(*args)
def texture(*args): _P5.texture(*args)
def textureMode(*args): _P5.textureMode(*args)
def vertex(*args): _P5.vertex(*args)

# Loading & Displaying
def image(*args): _P5.image(*args)
def imageMode(*args): _P5.imageMode(*args)
def loadImage(*args): return _P5.loadImage(*args)
def noTint(*args): _P5.noTint(*args)
def requestImage(*args): return _P5.requestImage(*args)
def tint(*args): _P5.tint(*args)

# Pixels
def blend(*args): _P5.blend(*args)
def copy(*args): _P5.copy(*args)
def filter(*args): _P5.filter(*args)
def get(*args): return _P5.get(*args)
def loadPixels(*args): _P5.loadPixels(*args)

## Color

# Setting
def background(*args): _P5.background(*args)
def colorMode(*args): _P5.background(*args)
def fill(*args): _P5.fill(*args)
def noFill(*args): _P5.noFill(*args)
def noStroke(*args): _P5.noStroke(*args)
def stroke(*args): _P5.stroke(*args)

# Creating & Reading
def alpha(*args): return _P5.alpha(*args)
def blendColor(*args): return _P5.blendColor(*args)
def blue(*args): return _P5.blue(*args)
def brightness(*args): return _P5.brightness(*args)
def color(*args): return _P5.color(*args)
def green(*args): return _P5.green(*args)
def hue(*args): return _P5.hue(*args)
def lerpColor(*args): return _P5.lerpColor(*args)
def red(*args): return _P5.red(*args)
def saturation(*args): return _P5.saturation(*args)

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
def dist(*args): return _P5.dist(*args)

# Random
def noise(*args): return _P5.noise(*args)
def noiseDetail(*args): return _P5.noiseDetail(*args)
def noiseSeed(*args): return _P5.noiseSeed(*args)
def random(*args): return _P5.random(*args)

# define constants
JAVA2D = 'processing.core.PGraphicsJava2D'


class MouseVars():
    x = -1
    y = -1
    px = None
    py = None
    btn = 0
    pressed = False

mouse = MouseVars()


class Environment(object):

    @staticmethod
    def map(*args):
        return _P5.map(*args)

    def __getattr__(self, name):
        if name in ('frameRate', 'frameCount', 'width', 'height', 'pixels'):
            return _P5.getField(name)
        else:
            return getattr(super(Environment, self), name)

P5 = Environment()


def P5_set_instance(inst):
    global _P5
    _P5 = inst


def P5_register_mouse_event(evt):
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


def run(sketch):
    from javax.swing import JFrame
    from processing.core import PApplet

    class Main(PApplet):

        def __init__(self, sketch):
            self.sketch = sketch
            P5_set_instance(self)

        def setup(self):
            self.sketch['setup']()

        def draw(self):
            self.sketch['draw']()

        def mousePressed(self, evt):
            P5_register_mouse_event(evt)
            self.sketch['mousePressed']()

        def mouseReleased(self, evt):
            P5_register_mouse_event(evt)

        def mouseClicked(self, evt):
            P5_register_mouse_event(evt)
            self.sketch['mouseClicked']()

        def mouseEntered(self, evt):
            P5_register_mouse_event(evt)

        def mouseExited(self, evt):
            P5_register_mouse_event(evt)

        def mouseDragged(self, evt):
            P5_register_mouse_event(evt)
            self.sketch['mouseDragged'](evt)

        def mouseMoved(self, evt):
            P5_register_mouse_event(evt)
            self.sketch['mouseMoved'](evt)

        def getField(self, name):
            # rqd due to PApplet's using frameRate and frameRate(n) etc.
            return self.class.superclass.getDeclaredField(name).get(self)

    if __name__ == '__main__' or True:
        frame = JFrame(title="Processing",
            resizable=0,
            defaultCloseOperation=JFrame.EXIT_ON_CLOSE)
        panel = Main(sketch)
        frame.add(panel)
        panel.init()
        while panel.defaultSize and not panel.finished:
            pass
        frame.pack()
        frame.visible = 1


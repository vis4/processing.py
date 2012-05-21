from javax.swing import JFrame
from processing.core import PApplet
from sketch import setup, draw, mouseClicked, mousePressed, mouseMoved, mouseDragged
from sketch import p9_set_instance, p9_register_mouse_event, p9_update_env


class Main(PApplet):

    def __init__(self):
        p9_set_instance(self)

    def setup(self):
        setup()

    def draw(self):
        p9_update_env()
        draw()

    def mousePressed(self, evt):
        p9_register_mouse_event(evt)
        mousePressed()

    def mouseReleased(self, evt):
        p9_register_mouse_event(evt)

    def mouseClicked(self, evt):
        p9_register_mouse_event(evt)
        mouseClicked()

    def mouseEntered(self, evt):
        p9_register_mouse_event(evt)

    def mouseExited(self, evt):
        p9_register_mouse_event(evt)

    def mouseDragged(self, evt):
        p9_register_mouse_event(evt)
        mouseDragged(evt)

    def mouseMoved(self, evt):
        p9_register_mouse_event(evt)
        mouseMoved(evt)

    def getField(s, name):
        # rqd due to PApplet's using frameRate and frameRate(n) etc.
        return s.class.superclass.getDeclaredField(name).get(s)

    @property
    def framerate(self):
        return self.getField('framerate')


if __name__ == '__main__':
    frame = JFrame(title="Processing",
        resizable=0,
        defaultCloseOperation=JFrame.EXIT_ON_CLOSE)
    panel = Main()
    frame.add(panel)
    panel.init()
    while panel.defaultSize and not panel.finished:
        pass
    frame.pack()
    frame.visible = 1

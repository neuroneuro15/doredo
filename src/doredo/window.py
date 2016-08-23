import pyglet
import pyglet.gl as gl


class Window(pyglet.window.Window):

    def __init__(self, *args, bgColor=(0.3, 0.7, 0.4, 1.), **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.bgColor = bgColor

    def clear(self, *args, **kwargs):
        super(Window, self).clear(*args, **kwargs)
        gl.glClearColor(*self.bgColor)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
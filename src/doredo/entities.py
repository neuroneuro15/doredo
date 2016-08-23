from pyglet import graphics
import pyglet.gl as gl


class Entity(object):

    def __init__(self, verts, x=0., y=0., color=(255, 255, 255)):
        self.verts = verts
        self.color = color
        self.x = x
        self.y = y
        self._vertex_list = None

    @property
    def vertex_list(self):
        if type(self._vertex_list) != type(None):
            return self._vertex_list
        else:
            n_verts = int(len(self.verts) / 2)
            self._vertex_list = graphics.vertex_list(3, #int(n_verts),
                                                     ('v2f', self.verts),
                                                     ('c3B', self.color * n_verts)
                                                     )
            return self._vertex_list


    def draw(self, mode=gl.GL_TRIANGLES):
        self.vertex_list.draw(mode=mode)

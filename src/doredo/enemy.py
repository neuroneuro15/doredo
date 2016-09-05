from . import resources, utils
from .entities import Entity
import pyglet.gl as gl
import numpy as np

class Rect(Entity):

    def __init__(self, *args, **kwargs):
        verts = resources.get_ngon_vertices(4)
        verts = utils.add_depth(verts)



        super(Rect, self).__init__(verts=verts, *args, **kwargs)
        self.normals = np.array(self.vertices) * -1

        self.obj.sx = self.obj.scale * 2 if abs(self.obj.x) > 1. else self.obj.sx
        self.obj.sy = self.obj.scale * 2 if abs(self.obj.y) > 1. else self.obj.sy


    def draw(self, shader, mode=gl.GL_TRIANGLE_FAN):
        super(Rect, self).draw(shader=shader, mode=mode)

    def move(self, distance):

        if self.obj.sx > self.obj.sy:
            self.obj.x += distance
        else:
            self.obj.y += distance


def rect_factory(loc_str='--*', side='d', startdist=1.5, scale=.2):
    """
    Generates rectangles, based on a locatoin string and side
    loc_str: '--*' means two rects in first two positions.  '*-*' means one rect in middle position.
    side= {'l', 'r', 'u', 'd'
    """

    rects = []


    for pos, fmt in zip([-.5, 0., .5], loc_str):

        if fmt == '-':
            if side == 'l':
                dd = {'x': -startdist, 'y': pos}
            elif side == 'r':
                dd = {'x': startdist, 'y': pos}
            elif side == 'u':
                dd = {'x': pos, 'y': startdist}
            elif side == 'd':
                dd = {'x': pos, 'y': -startdist}

            rect = Rect(scale=scale, **dd)
            rects.append(rect)

    return rects



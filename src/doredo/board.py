from .entities import Entity
import pyglet.gl as gl
import itertools as it
from . import resources, utils
import numpy as np

class Board(object):

    def __init__(self, spacing=.5, pointsides=5, scale=.2, color=(1., 0., .5)):
        self.positions = list(it.product(*[[-spacing, 0, spacing]] * 2))

        self.spots = []
        for x, y in self.positions:
            verts = resources.get_ngon_vertices(pointsides)
            verts = utils.add_depth(verts)

            spot = Entity(verts, x=x, y=y, scale=scale, color=color)
            spot.normals = np.array(spot.vertices) * -1
            self.spots.append(spot)

    def draw(self, shader, mode=gl.GL_TRIANGLE_FAN):

        for spot in self.spots:
            spot.draw(shader, mode=mode)

    @property
    def rot(self):
        return self.spots[0].obj.rot

    @rot.setter
    def rot(self, value):
        for spot in self.spots:
            spot.obj.rot = value
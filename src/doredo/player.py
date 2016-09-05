from .entities import Entity
from . import resources, utils
import pyglet.gl as gl
import numpy as np

class Player(Entity):

    def __init__(self, *args, **kwargs):

        verts = resources.get_ngon_vertices(5)
        verts = utils.add_depth(verts)

        super(Player, self).__init__(verts=verts, *args, **kwargs)
        self.normals = np.array(self.vertices) * -1

    def draw(self, shader, mode=gl.GL_TRIANGLE_FAN):
        super(Player, self).draw(shader, mode=mode)


from pyglet import graphics
import pyglet.gl as gl
from functools import partial
import numpy as np


class Entity(object):

    def __init__(self, verts, x=0., y=0., color=(1., 1., 1.)):
        self.vertex_list = self._build_vertex_list(verts, color)
        self.x = x
        self.y = y
        self.__keyframe = 0.


    @property
    def vertices(self):
        return self.vertex_list.vertices[:]

    @vertices.setter
    def vertices(self, verts):
        self.vertex_list.vertices[:] = verts

    @property
    def normals(self):
        return self.vertex_list.normals[:]

    @normals.setter
    def normals(self, verts):
        self.vertex_list.normals[:] = verts

    @property
    def color(self):
        return self.vertex_list.colors[:3]

    @color.setter
    def color(self, values):
        n_verts = int(len(self.vertex_list.vertices) / 3)
        self.vertex_list.colors[:] = values * n_verts


    @property
    def keyframe(self):
        return self.__keyframe

    @keyframe.setter
    def keyframe(self, value):
        assert 0. <= value <= 1.
        self.__keyframe = value

    def _build_vertex_list(self, verts, color=(.1, .1, .5)):
        vv = np.array(verts).ravel()
        n_verts = int(vv.size / 3)
        update_mode = 'dynamic'

        vertex_list = graphics.vertex_list(n_verts,
                                                 ('v3f/{}'.format(update_mode), vv),
                                                 ('c3f', color * n_verts),
                                                 ('n3f/{}'.format(update_mode), vv),
                                                 )
        return vertex_list


    def draw(self, shader, mode=gl.GL_TRIANGLES):
        shader.uniformf('keyframe', self.keyframe)
        self.vertex_list.draw(mode=mode)

    def update(self, dt):
        pass



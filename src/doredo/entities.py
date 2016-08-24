from pyglet import graphics
import pyglet.gl as gl
from functools import partial
import numpy as np


class Entity(object):

    dynamic = False

    def __init__(self, verts, x=0., y=0., color=(255, 255, 255)):


        self._verts = self._process_vertlist_to_3d_array(verts)

        self.color = color
        self.x = x
        self.y = y
        self._vertex_list = None

    @property
    def dynamic(self):
        return False

    @staticmethod
    def _process_vertlist_to_3d_array(verts):
        vv = np.array(verts, dtype=float).reshape(-1, 2)  # Make a n x 2 array of vertices
        vv = np.hstack((vv, np.zeros((vv.shape[0], 1))))  # Add a third column of zeros: that's its depth.
        return vv

    @property
    def vertices(self):
        return self._verts

    @vertices.setter
    def vertices(self, verts):
        self._verts = self._process_vertlist_to_3d_array(verts)
        self.vertex_list.vertices[:] = self._verts.ravel()
        self.vertex_list.normals[:] = self._verts.ravel()


    @property
    def vertex_list(self):
        if type(self._vertex_list) != type(None):
            return self._vertex_list
        else:
            n_verts = self._verts.shape[0]
            update_mode = 'dynamic' if self.dynamic else 'static'

            self._vertex_list = graphics.vertex_list(n_verts,
                                                     ('v3f/{}'.format(update_mode), self._verts.ravel()),
                                                     ('c3B', self.color * n_verts),
                                                     ('n3f/{}'.format(update_mode), self._verts.ravel()),
                                                     )
            return self._vertex_list


    def draw(self, mode=gl.GL_TRIANGLES):
        self.vertex_list.draw(mode=mode)


    def update(self, dt):
        pass



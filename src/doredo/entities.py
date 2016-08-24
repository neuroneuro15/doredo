from pyglet import graphics
import pyglet.gl as gl
from functools import partial
import numpy as np


class Physical(object):

    __observables = ('x', 'y', 'rot', 'scale')

    def __init__(self, x=0., y=0., rot=0., scale=1.):
        self.__dict__['x'] = x
        self.__dict__['y'] = y
        self.__dict__['rot'] = rot
        self.__dict__['scale'] = scale

        self.modelmat = None
        self.update()

    def __setattr__(self, key, value):
        super(Physical, self).__setattr__(key, value)

        if key in Physical.__observables:
            self.on_change()

    def on_change(self):
        """
        This method fires when object position or geometry changes.
        Can be overwritten by parent classes to add more actions.
        """
        self.update()

    def update(self):
        x, y, s, rot = self.x, self.y, self.scale, self.rot
        mm = np.array([[s * np.cos(rot), -np.sin(rot), 0, x],
                       [np.sin(rot),  s * np.cos(rot), 0, y],
                       [              0,            0, s, 0],
                       [              0,            0, 0, 1]
                      ])
        self.modelmat = mm



class Entity(object):

    def __init__(self, verts, x=0., y=0., rot=0., scale=1., color=(1., 1., 1.)):
        self.vertex_list = self._build_vertex_list(verts, color)
        self.obj = Physical(x=x, y=y, rot=rot, scale=scale)
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
        shader.uniform_matrixf('modelmat', self.obj.modelmat.T.ravel())
        self.vertex_list.draw(mode=mode)

    def update(self, dt):
        pass



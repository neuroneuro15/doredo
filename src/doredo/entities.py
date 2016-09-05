from pyglet import graphics
import pyglet.gl as gl
from functools import partial
import numpy as np


class Physical(object):

    __observables = ('x', 'y', 'rot', 'sx', 'sy')

    def __init__(self, x=0., y=0., rot=0., scale=1.):
        self.__dict__['x'] = x
        self.__dict__['y'] = y
        self.__dict__['rot'] = rot
        self.__dict__['sx'] = scale
        self.__dict__['sy'] = scale


        self.modelmat = None
        self.update()



    def __setattr__(self, key, value):
        super(Physical, self).__setattr__(key, value)

        if key in Physical.__observables:
            self.on_change()

    @property
    def scale(self):
        return self.sx

    @scale.setter
    def scale(self, *value):
        if len(value) == 1:
            self.sx = value[0]
            self.sy = value[0]
        else:
            self.sx, self.sy = value


    def on_change(self):
        """
        This method fires when object position or geometry changes.
        Can be overwritten by parent classes to add more actions.
        """
        self.update()

    def update(self):
        x, y, sx, sy, rot = self.x, self.y, self.sx, self.sy, self.rot
        trans = np.array([[1., 0, 0, x],
                          [0, 1., 0, y],
                          [0, 0, 1., 0],
                          [0, 0, 0, 1.]], dtype=float)

        rot = np.array([[np.cos(rot), -np.sin(rot), 0, 0],
                       [np.sin(rot), np.cos(rot), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]], dtype=float)

        scale = np.array([[sx, 0, 0, 0],
                          [0, sy, 0, 0],
                          [0, 0, 1., 0],
                          [0, 0, 0, 1]], dtype=float)

        # self.modelmat = np.dot(scale, np.dot(rot, trans))
        self.modelmat = np.dot(trans, np.dot(rot, scale))



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



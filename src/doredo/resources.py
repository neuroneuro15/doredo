import os
from os import path
from .shader import Shader
import numpy as np

triangle = (-1., -1.,
            1., -1.,
            0., 1.)

square = (-1., 1.,
          1.,  1.,
         -1., -1.,
         -1., -1.,
          1., -1.,
          1.,  1.)

def rotate2d(x, y, theta):
    rotmat = np.array([[np.cos(theta), -np.sin(theta)],
                       [np.sin(theta), np.cos(theta)]])
    return np.dot(rotmat, np.array([[x, y]], dtype=float).T).flatten()

def get_ngon_vertices(sides):
    """Returns triangle strip order for any polygon"""
    assert sides > 2
    angles = np.linspace(0, 2 * np.pi, sides + 1)
    verts = np.vstack(([0., 0.], [rotate2d(1, 0, theta=angle) for angle in angles]))
    # verts -= np.mean(verts, axis=0)
    return verts


shader_path = path.join(path.split(__file__)[0], 'shaders')

genShader = Shader(vert=open(path.join(shader_path, 'standard.vert')).read(),
                   frag=open(path.join(shader_path, 'standard.frag')).read()
                   )
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

def get_ngon_vertices(sides):
    assert sides > 3
    angles = np.linspace(0, 2 * np.pi / sides




shader_path = path.join(path.split(__file__)[0], 'shaders')

genShader = Shader(vert=open(path.join(shader_path, 'standard.vert')).read(),
                   frag=open(path.join(shader_path, 'standard.frag')).read()
                   )
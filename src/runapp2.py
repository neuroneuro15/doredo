import pyglet
import numpy as np
from doredo import Shader, Entity, Window, cumclock, utils, resources
import itertools as it



window = Window(bgColor=(.3, .7, .4, 1.), vsync=False)

triangles = []
for x, y in it.product((-.5, .5), (-.5, 0., .5)):
    triangle = utils.gen_primitive_entity('triangle', x=x, y=y, scale=.2)
    triangles.append(triangle)


shader = resources.genShader

@window.event
def on_draw():
    window.clear()
    with shader as shad:
        for triangle in triangles:
            triangle.draw(shad)


def update(dt):
    pass


pyglet.clock.schedule(update)


pyglet.app.run()

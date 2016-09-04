import pyglet
import numpy as np
from doredo import Shader, Entity, Window, cumclock, utils, resources, BarClock, BeatClock
import itertools as it

# metronome = BarClock(bpm=200, beats=4)
metronome = BeatClock(bpm=100)


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
    triangles[0].obj.scale = metronome.tick() / 4.
    triangles[1].obj.scale = (metronome.tick() ** 2) / 4.
    triangles[2].obj.scale = np.sin(metronome.tick() * np.pi) / 4.
    triangles[3].obj.scale = (np.sin(metronome.tick() * np.pi) / 8.) + .125
    triangles[4].obj.scale = (np.abs(metronome.tick() - .5) + .5) / 4.
    triangles[5].obj.rot += dt * 3.

    # for triangle in triangles:
    #     triangle.obj.scale = np.sin(metronome.tick() * np.pi)
pyglet.clock.schedule(update)


pyglet.app.run()

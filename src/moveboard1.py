import pyglet
from pyglet.window import key
import pyglet.gl as gl
import numpy as np
from doredo import Shader, Entity, Window, cumclock, utils, resources
import itertools as it


window = pyglet.window.Window()
shader = resources.genShader

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



spacing = .5
board = Board(pointsides=80, spacing=spacing, scale=.02)

# Make player
verts = resources.get_ngon_vertices(5)
verts = utils.add_depth(verts)

player = Entity(verts, x=0, y=0, scale=.2, color=(.2, .9, .3))
player.normals = np.array(player.vertices) * -1



@window.event
def on_draw():
    window.clear()
    with shader:
        board.draw(shader)
        player.draw(shader, mode=gl.GL_TRIANGLE_FAN)


def update(dt):
    player.obj.rot += dt * 2
pyglet.clock.schedule(update)

keys = key.KeyStateHandler()
window.push_handlers(keys)
def get_keyboard(dt):
    if keys[key.UP]:
        player.obj.y = spacing
    elif keys[key.DOWN]:
        player.obj.y = -spacing
    else:
        player.obj.y = 0.
    if keys[key.RIGHT]:
        player.obj.x = spacing
    elif keys[key.LEFT]:
        player.obj.x = -spacing
    else:
        player.obj.x = 0.
pyglet.clock.schedule(get_keyboard)


pyglet.app.run()
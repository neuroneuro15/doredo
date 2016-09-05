import pyglet
from pyglet.window import key
import numpy as np
import pyglet.gl as gl
from doredo import Shader, Entity, Window, cumclock, utils, resources, Board, Player
import itertools as it
import random
window = pyglet.window.Window()
shader = resources.genShader


spacing = .5
board = Board(pointsides=80, spacing=spacing, scale=.02)

player = Player(scale=.15, color=(.2, .7, .2))


class Rect(Entity):

    def __init__(self, *args, **kwargs):
        verts = resources.get_ngon_vertices(4)
        verts = utils.add_depth(verts)



        super(Rect, self).__init__(verts=verts, *args, **kwargs)
        self.normals = np.array(self.vertices) * -1

        self.obj.sx = self.obj.scale * 2 if abs(self.obj.x) > 1. else self.obj.sx
        self.obj.sy = self.obj.scale * 2 if abs(self.obj.y) > 1. else self.obj.sy


    def draw(self, shader, mode=gl.GL_TRIANGLE_FAN):
        super(Rect, self).draw(shader=shader, mode=mode)


positions = list(it.product(*[[-spacing, 0, spacing]] * 2))
positions.pop(4)  # Remove (0,0)
boxes = []
speed = 1.2
def box_launcher(dt):
    if not boxes:
        dim = random.randint(1, 2)
        for el in range(random.randint(1,2)):
            x,y = random.choice(positions)


            if dim == 1:
                box = Rect(x=-1.5, y=y, scale=.2)
            else:
                box = Rect(x=-x, y=-1.5, scale=.2)
            boxes.append(box)
            print('creating box..')

    for box in boxes:
        if box.obj.sx > box.obj.sy:
            box.obj.x += speed * dt
        else:
            box.obj.y += speed * dt

    if box.obj.x > 2. or box.obj.y > 2.:
        bb = boxes.pop()
        del bb
pyglet.clock.schedule(box_launcher)

@window.event
def on_draw():
    window.clear()
    with shader:
        board.draw(shader)
        player.draw(shader)
        for box in boxes:
            box.draw(shader)


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
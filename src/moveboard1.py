import pyglet
from pyglet.window import key
from doredo import Shader, Entity, Window, cumclock, utils, resources, Board, Player


window = pyglet.window.Window()
shader = resources.genShader


spacing = .5
board = Board(pointsides=80, spacing=spacing, scale=.02)

player = Player(scale=.2, color=(.2, .7, .2))

@window.event
def on_draw():
    window.clear()
    with shader:
        board.draw(shader)
        player.draw(shader)


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
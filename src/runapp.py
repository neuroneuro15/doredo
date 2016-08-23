import pyglet
import numpy as np
from doredo import Shader, Entity, Window, CumClock



window = Window(bgColor=(.3, .7, .4, 1.), vsync=False)


triangle_verts = (-1., -1.,
                  1., -1.,
                  0., 1.)

player = Entity(triangle_verts)


vert = """
#version 330 core
layout(location = 0) in vec2 vertexPosition_modelspace;
void main(){
    gl_Position.xy = vertexPosition_modelspace;
    gl_Position.z = 0.0;
    gl_Position.w = 1.0;
}
"""

frag = """
#version 330 core
out vec3 color;
void main(){
  color = vec3(1,0,0);
}
"""

shader = Shader(vert=vert, frag=frag)

@window.event
def on_draw():
    window.clear()
    with shader:
        player.draw()


timer = CumClock()
pyglet.clock.schedule(timer.tick)

def update(dt):
    new_verts = [np.sin(timer.cumtime) * v for v in triangle_verts]
    player.vertex_list.vertices[:] = new_verts
pyglet.clock.schedule(update)

pyglet.app.run()

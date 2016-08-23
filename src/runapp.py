import pyglet
import pyglet.gl as gl
from doredo import Shader, Entity, Window



window = Window(bgColor=(.3, .7, .4, 1.))


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

def update(dt):
    pass
pyglet.clock.schedule(update)

pyglet.app.run()

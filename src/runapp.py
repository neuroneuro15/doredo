import pyglet
import numpy as np
from doredo import Shader, Entity, Window, cumclock, utils



window = Window(bgColor=(.3, .7, .4, 1.), vsync=False)


triangle_verts = (-1., -1.,
                  1., -1.,
                  0., 1.)
triangle_verts = utils.add_depth(triangle_verts)

player = Entity(triangle_verts, color=(1., 0., .5))
player.normals = np.array(player.vertices) * -1
# new_verts = [np.sin(cumclock.cumtime) * v for v in triangle_verts]


vert = """
#version 330 core
layout(location = 0) in vec3 vert0;
layout(location = 2) in vec3 vert1;
layout(location = 3) in vec3 col;

out vec3 col2;

uniform float keyframe;
void main(){

    gl_Position.xyz = mix(vert0, vert1, keyframe);
    gl_Position.w = 1.0;

    col2 = col;
}
"""

frag = """
#version 330 core
out vec3 color;
in vec3 col2;
void main(){
//  color = vec3(1,0,0);
    color = col2;
}
"""

shader = Shader(vert=vert, frag=frag)

@window.event
def on_draw():
    window.clear()
    with shader as shad:
        player.draw(shad)


def update(dt):
    player.update(dt)
    player.keyframe = .5 * np.sin(cumclock.cumtime) + 0.5


pyglet.clock.schedule(update)


pyglet.app.run()

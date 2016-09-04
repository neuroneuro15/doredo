import pyglet
import numpy as np
from doredo import Shader, Entity, Window, cumclock, utils, resources




window = Window(bgColor=(.3, .7, .4, 1.), vsync=False)

triangle_verts = (-1., -1.,
                  1., -1.,
                  0., 1.)
triangle_verts = utils.add_depth(resources.triangle)

player = Entity(triangle_verts, color=(1., 0., .5))
player.normals = np.array(player.vertices) * -1
player.obj.scale = .2
# player.obj.x = .7

# new_verts = [np.sin(cumclock.cumtime) * v for v in triangle_verts]


vert = """
#version 330 core
layout(location = 0) in vec3 vert0;
layout(location = 2) in vec3 vert1;
layout(location = 3) in vec3 col;

out vec3 col2;

uniform float keyframe;
uniform mat4 modelmat;

void main(){

    vec4 vertex = vec4(mix(vert0, vert1, keyframe), 1.0);
    gl_Position = modelmat * vertex;

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
    # player.keyframe = .5 * np.sin(cumclock.cumtime) + 0.5
    player.obj.rot += np.pi * dt


pyglet.clock.schedule(update)


pyglet.app.run()

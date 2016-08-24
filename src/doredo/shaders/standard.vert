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
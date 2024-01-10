#version 330 core
in vec3 position;
in vec4 colors;
out vec4 vertex_colors;

uniform mat4 projection;

void main()
{
    gl_Position = projection * vec4(position, 1.0);
    vertex_colors = colors;
}
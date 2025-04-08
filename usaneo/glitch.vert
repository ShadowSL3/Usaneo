#version 120
uniform sampler2D tex;
uniform float time;
varying vec2 uv;

void main() {
    vec2 glitch_uv = uv;
    glitch_uv.x += sin(glitch_uv.y * 10.0 + time * 5.0) * 0.01;
    glitch_uv.y += cos(glitch_uv.x * 10.0 + time * 2.0) * 0.01;
    gl_FragColor = texture2D(tex, glitch_uv);
}
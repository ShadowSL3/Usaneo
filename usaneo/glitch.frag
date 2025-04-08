// glitch.frag
#version 120

uniform sampler2D tex;  // Texture sorgente
uniform float time;     // Tempo dinamico passato da pygame_shaders
varying vec2 uv;        // Coordinate UV interpolate

void main() {
    // Effetto di shift orizzontale glitchato
    float strength = 0.02;
    float y_offset = sin(uv.y * 40.0 + time * 5.0) * strength;
    float x_offset = cos(uv.y * 10.0 + time * 2.0) * strength * 0.5;

    vec2 glitch_uv = uv + vec2(y_offset, x_offset);

    // Chromatic aberration semplice
    float r = texture2D(tex, glitch_uv + vec2(0.005, 0.0)).r;
    float g = texture2D(tex, glitch_uv).g;
    float b = texture2D(tex, glitch_uv - vec2(0.005, 0.0)).b;

    gl_FragColor = vec4(r, g, b, 1.0);
}
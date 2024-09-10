import pygame

class Vec2:
     def __init__(self, vec2):
        self.vec2 = pygame.math.Vector2
        
class Vec3:
    def __init__(self, vec3, value_clamp:float, min_clamp:float, max:float):
        self.vec3 = pygame.math.Vector3
        self.clam = pygame.math.clamp(value_clamp, min_clamp, max)
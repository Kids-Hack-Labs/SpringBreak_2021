from pygame import Color, Rect, Surface
from pygame.locals import *
import pygame.key as pk
import pygame.draw as pd

class Player():
    def __init__(self):
        self.rect = Rect(0, 0, 50, 50)
        self.colour = Color(0, 255, 0)
        self.surf = Surface(self.rect.size)

        self.surf.fill(self.colour)

        self.vel = [0.25, 0.25] #rework!

        self.max_time = 100
        self.cur_time = 100
        self.directions = ((0,-1),(1,0),(0,1),(-1,0))
        self.cur_direction = None
        self.command_queue = []

    def update(self, delta):
        keys = pk.get_pressed()

        up = keys[K_w] or keys[K_UP]
        right = keys[K_d] or keys[K_RIGHT]
        down = keys[K_s] or keys[K_DOWN]
        left = keys[K_a] or keys[K_LEFT]

        self.rect.left += self.vel[0] * delta * (right - left) #REWORK
        self.rect.top += self.vel[1] * delta * (down - up) #REWORK

    def render(self, target):
        target.blit(self.surf, self.rect)

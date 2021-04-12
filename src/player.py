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

    def update(self):
        pass

    def render(self, target):
        target.blit(self.surf, self.rect)

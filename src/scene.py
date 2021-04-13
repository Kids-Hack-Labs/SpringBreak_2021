from pygame.locals import *
from pygame import Color, Rect, Surface
from src.player import Player

class Scene():
    def __init__(self, text_info = None, scene_info = None):
        self.surf = Surface((800,800), SRCALPHA)
        #GRID:
        number_of_cells = 16
        from pygame.draw import rect as pdr
        for i in range(number_of_cells):
            for j in range(number_of_cells):
                if (i%2==0) ^ (j%2==0):
                    pdr(self.surf, (255, 255, 255), Rect(i*50, j*50, 50, 50))
        
        #Player
        self.player = Player()

    def update(self, delta):
        self.player.update(delta)
    
    def render(self, target):
        target.fill((127, 127, 127))
        target.blit(self.surf, (0,0))
        self.player.render(target)

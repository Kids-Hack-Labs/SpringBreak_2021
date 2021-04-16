from pygame.locals import *
from pygame import Color, Rect, Surface
from src.player import Player
from src.level import Level

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

        #Level
        self.level = Level()

        #Win condition
        self.won = False

    def update(self, delta):
        if self.won:
            return
        
        self.level.update(delta)

        coords = self.player.get_coords()
        self.player.set_pos_data(self.level.get_at(coords))
        
        self.player.update(delta)

        self.won = self.player.get_coords() == self.level.win_tile
    
    def render(self, target):
        target.fill((200, 200, 200))
        target.blit(self.surf, (0,0))

        if self.won:
            target.fill((0,255,0))
        
        self.level.render(target)
        self.player.render(target)

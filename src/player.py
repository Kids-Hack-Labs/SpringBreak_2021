from pygame import Color, Rect, Surface
from pygame.locals import *
import pygame.key as pk
import pygame.draw as pd

class Player():
    def __init__(self):
        self.rect = Rect(0, 0, 50, 50)
        self.bg_colour = Color(0, 255, 0)
        self.colour = Color(127, 0, 255)
        self.surf = Surface(self.rect.size)
        self.rect = self.surf.get_rect()

        self.surf.fill(self.bg_colour)
        self.surf.set_colorkey(self.bg_colour)
        pd.circle(self.surf, self.colour, self.rect.center, 24)

        self.max_time = 250
        self.cur_time = 250
        self.directions = ((0,-1),(1,0),(0,1),(-1,0))
        self.cur_direction = None
        self.command_queue = []

        self.position = [7,0]
        self.position_data = 0
        self.update_player_position()

    def update(self, delta):
        keys = pk.get_pressed()

        up = keys[K_w] or keys[K_UP]
        right = keys[K_d] or keys[K_RIGHT]
        down = keys[K_s] or keys[K_DOWN]
        left = keys[K_a] or keys[K_LEFT]

        self.command_player((up, right, down, left))
        self.update_player(delta)
        
        self.update_player_position()

    def render(self, target):
        target.blit(self.surf, self.rect)

    def command_player(self, dirs):
        if not self.command_queue: #If command queue is empty
            for i in range(len(dirs)):
                if dirs[0]: #up
                    self.command_queue.append(1)
                    return
                if dirs[1]: #right
                    self.command_queue.append(2)
                    return
                if dirs[2]: #down
                    self.command_queue.append(4)
                    return
                if dirs[3]: #left
                    self.command_queue.append(8)
                    return

    def update_player(self, delta):
        self.cur_time -= delta
        if self.cur_time <= 0:
            self.cur_time += self.max_time
            self.move_player()

    def move_player(self):
        offset = (0,0)
        if self.command_queue:
            condition = self.command_queue.pop(0)
            if condition & self.position_data:
                return
            if condition == 1:
                offset = self.directions[0]
            if condition == 2:
                offset = self.directions[1]
            if condition == 4:
                offset = self.directions[2]
            if condition == 8:
                offset = self.directions[3]

        self.position[0] += offset[0]
        self.position[1] += offset[1]

    def update_player_position(self):
        self.rect.left = self.position[0]*50
        self.rect.top = self.position[1]*50

    def get_coords(self):
        return self.position

    def set_pos_data(self, data):
        self.position_data = data

















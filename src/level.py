import csv
from pygame import Color, Rect, Surface
import pygame.draw as pd

class Level():
    def __init__(self):
        self.surf = Surface((800,800))
        background = Color(0, 0, 255)
        self.surf.fill(background)
        self.surf.set_colorkey(background)

        self.cell_size = 50

        origin = Rect(7*self.cell_size, 0*self.cell_size,
                      self.cell_size, self.cell_size)
        pd.rect(self.surf, Color(255, 0, 0), origin)
        destination = Rect(8*self.cell_size, 15*self.cell_size,
                           self.cell_size, self.cell_size)
        pd.rect(self.surf, Color(0, 255, 0), destination)

        self.line_colour = Color(0, 0, 0)
        self.line_thickness = 2
        self.level_data = []

        self.win_tile = [8,15]

        with open("./src/data/level.csv", newline="") as ld:
            level_reader = csv.reader(ld, skipinitialspace=True)
            self.level_data.extend([[int(cell) for cell in row]
                                    for row in level_reader])

        for i in range(len(self.level_data)):
            for j in range(len(self.level_data[i])):
                if self.level_data[i][j] & 1: #bitwise AND
                    pd.line(self.surf, self.line_colour,
                            (j*self.cell_size, i*self.cell_size),
                            ((j+1)*self.cell_size-1, i*self.cell_size),
                            self.line_thickness)
                if self.level_data[i][j] & 2: #bitwise AND
                    pd.line(self.surf, self.line_colour,
                            ((j+1)*self.cell_size-1, i*self.cell_size),
                            ((j+1)*self.cell_size-1, (i+1)*self.cell_size-1),
                            self.line_thickness)
                if self.level_data[i][j] & 4: #bitwise AND
                    pd.line(self.surf, self.line_colour,
                            ((j+1)*self.cell_size-1, (i+1)*self.cell_size-1),
                            (j*self.cell_size, (i+1)*self.cell_size-1),
                            self.line_thickness)
                if self.level_data[i][j] & 8: #bitwise AND
                    pd.line(self.surf, self.line_colour,
                            (j*self.cell_size, (i+1)*self.cell_size-1),
                            (j*self.cell_size, i*self.cell_size),
                            self.line_thickness)

    def update(self, delta):
        pass

    def render(self,target):
        target.blit(self.surf,(0,0))

    def get_at(self, position):
        return self.level_data[position[1]][position[0]]









                

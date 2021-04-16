import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface
import pygame.key as pk
import pygame.draw as pd
from pygame.time import Clock
from pygame.font import Font

FPS = 30
def main():
    pygame.init()
    screen_size = (400, 400)
    screen = pygame.display.set_mode(screen_size)
    screen_rect = screen.get_rect()
    
    pygame.display.set_caption("cell study")

    clock = Clock()
    delta = 0

    cell_amt = (8, 8)
    
    cell_size = (int(screen_size[0]/cell_amt[0]),
                 int(screen_size[1]/cell_amt[1]))

    surf = Surface(screen.get_size())
    surf.fill((200, 200, 200))
    for x in range(cell_amt[0]):
        for y in range(cell_amt[1]):
            if (x%2==0)^(y%2==0):
                pd.rect(surf, (255, 255, 255),
                        Rect((x*cell_size[0], y*cell_size[1]),cell_size))

    control = 0
    max_time = 1000
    time = 1000

    font = Font(pygame.font.get_default_font(), 150)
    font_colour = Color(0, 0, 0)
    font_surf = None
    font_rect = None
    font_surf = font.render(str(control), True, font_colour, None)
    font_rect = font_surf.get_rect()
    font_rect.center = screen_rect.center

    line_colour = Color(255, 127, 0)
    line_width = 3

    running = True
        
    while running:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                running = False

        #update
        time -= delta
        if time <= 0:
            time += max_time
            control +=1
            control %= 16
            font_surf = font.render(str(control), True, font_colour, None)
            font_rect = font_surf.get_rect()
            font_rect.center = screen_rect.center

        #render
        screen.blit(surf, (0, 0))
        #DRAWN ON SCREEN AT RUNTIME
        if control & 1: #top
            pd.line(screen, line_colour, (100, 100),(300, 100), line_width)
        if control & 2: #right
            pd.line(screen, line_colour, (300, 100),(300, 300), line_width)
        if control & 4: #bottom
            pd.line(screen, line_colour, (300, 300),(100, 300), line_width)
        if control & 8: #left
            pd.line(screen, line_colour, (100, 300),(100, 100), line_width)

        screen.blit(font_surf, font_rect)
        pygame.display.flip()
        delta = clock.tick(FPS)
        
    pygame.quit()

if __name__ == "__main__":
    main()

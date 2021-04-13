#Note: As this module is imported into main.py, all paths become
#      relative to where main.py is
import pygame
from pygame.locals import *
from pygame.time import Clock
from engine.scene_manager import SceneManager
from src.scene import Scene

global FPS

class Game():
    class __Game():
        def __init__(self, defaults, window_properties):
            global FPS
            FPS = defaults["FPS"]

            self.is_start = False
            self.is_run = False
            self.delta = 0
            self.time_since_started = 0
            self.clock = Clock()

            pygame.init()
            screen_flags = window_properties["fullscreen"]*FULLSCREEN|\
                           window_properties["resizable"]*RESIZABLE|\
                           window_properties["scaled"]*SCALED|\
                           window_properties["opengl"]*OPENGL
            self.screen = pygame.display.set_mode((window_properties["width"],
                                                   window_properties["height"]),
                                                  screen_flags)
            pygame.display.set_caption(window_properties["caption"])
            self.time_since_started = pygame.time.get_ticks()

            SceneManager()
            
            self.scene = None
            self.is_run = True

        def start(self):
            temp = SceneManager.instance.request_scene_data(0, "TITLE")
            self.scene = Scene(temp[0], temp[1])
            self.is_start = pygame.get_init() and self.scene != None

        def process_events(self):
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    self.quit()
                    
        def update(self, delta):
            self.scene.update(delta)

        def render(self, target):
            self.scene.render(target)
            
            pygame.display.flip()

        def run(self):
            if self.is_start:
                return
            self.start()
            while self.is_run:
                self.process_events()
                self.update(self.delta)
                self.render(self.screen)
                self.delta = self.clock.tick(FPS)
                self.time_since_started = pygame.time.get_ticks()
            pygame.quit()

        def quit(self):
            self.is_run = False

        def request_next_scene(self):
            temp = SceneManager.instance.next_scene()
            self.scene = Scene(temp[0], temp[1])
            

    #Singleton:
    __instance = None
    def __init__(self, defaults, window_properties):
        if Game.__instance is None:
            Game.__instance = Game.__Game(defaults, window_properties)

    def __getattr__(self, name):
        return getattr(self.__instance, name)

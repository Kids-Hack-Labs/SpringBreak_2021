from src.player import Player

class Scene():
    def __init__(self, text_info = None, scene_info = None):
        self.player = Player()

    def update(self, delta):
        self.player.update()
    
    def render(self, target):
        target.fill((127, 127, 127))
        self.player.render(target)

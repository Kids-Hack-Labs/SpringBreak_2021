from src.player import Player

class Scene():
    def __init__(self, text_info, scene_info):
        self.player = Player()

    def update(self, delta):
        self.player.update()
    
    def render(self, target):
        target.fill((127, 127, 127))
        self.player.render(target)

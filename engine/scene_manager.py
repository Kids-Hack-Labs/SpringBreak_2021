import csv
import json

class SceneManager():
    instance = None
    class __SceneManager():
        is_init = False
        SCENE_TYPES = ()
        current_scene_index = 0
        def __init__(self):
            SceneManager.__SceneManager.is_init = True
            
        def get_init(self):
            return SceneManager.instance.is_init

        def request_scene_data(self, index, scene_type):
            #TODO: Devise new scene logic
            return [None, None]

        def next_scene(self):
            return self.request_scene_data(0, None)

    def __init__(self):
        if not SceneManager.instance:
            SceneManager.instance = SceneManager.__SceneManager()

    def __getattr__(self, name):
        return getattr(self.instance, name)

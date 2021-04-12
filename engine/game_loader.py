from configparser import ConfigParser
from engine.game_env import Game

class GameLoader():
    @staticmethod
    def load_game():
        config = ConfigParser()
        config.BOOLEAN_STATES={"enabled":True, "disabled":False}
        config.read("./engine/data/config.ini")
        defaults = config["DEFAULT"]
        default_properties = {"FPS":defaults.getint("FPS")}
        window_attributes = config["WINDOW SETTINGS"]
        window_properties = {"width":window_attributes.getint("width"),
                             "height":window_attributes.getint("height"),
                             "caption":window_attributes.get("title"),
                             "fullscreen":window_attributes.getboolean("fullscreen"),
                             "resizable":window_attributes.getboolean("resizable"),
                             "opengl":window_attributes.getboolean("opengl"),
                             "scaled":window_attributes.getboolean("scaled")}
        return Game(default_properties, window_properties)

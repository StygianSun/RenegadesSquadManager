from pathlib import Path
import os
import sys
from backend.models.squad import Squad
import yaml
import logging

logger = logging.getLogger(__name__)

class FileManager():
    def __init__(self):
        self.loaded_file = None

    def loadSquad(self):
        squad_data = None
        if self.loaded_file is None:
            raise ValueError("Loaded file not set")
        try:
            with open(self.loaded_file, 'r') as file:
                squad_data = yaml.safe_load(file)
            return squad_data
        except Exception as e:
            logger.exception(f"Failed to load squad from {self.loaded_file}: {e}")
    
    def saveSquad(self, squad: Squad = None):
        if squad.player_name == "" and (squad is None or squad.isEmpty()):
            raise ValueError("Cannot save an empty squad without a player name")
        if self.loaded_file is None:
            raise ValueError("Loaded file not set")
        squad_dict = {}
        squad_dict["player_name"] = squad.player_name
        squad_dict["squad"] = squad.toDict()
        try:
            with open(self.loaded_file, 'w') as file:
                yaml.dump(squad_dict, file, sort_keys=False)
        except Exception as e:
            logger.exception(f"Failed to save squad to {self.loaded_file}: {e}")
        
    @staticmethod
    def read_config_file(file: str = ''):
        if getattr(sys, 'frozen', False):
            config_file = Path(sys._MEIPASS) / "config" / file
        else:
            config_file = Path(os.getcwd()) / "backend" / "config" / "rules_configurations" / file
        data = None
        try:
            with open(config_file, 'r') as file:
                data = yaml.safe_load(file)
            return data
        except Exception as e:
            logger.exception(f"Failed to read config file {config_file}: {e}")
from pathlib import Path
import os
import sys
from backend.models.squad import Squad
import yaml

class FileManager():
    def __init__(self):
        self.loaded_file = None

    def loadSquad(self):
        squad_data = None
        with open(self.loaded_file, 'r') as file:
            squad_data = yaml.safe_load(file)
        return squad_data
    
    def saveSquad(self, squad: Squad = None):
        if squad.player_name == "" and (squad is None or squad.isEmpty()):
            return
        squad_dict = {}
        squad_dict["player_name"] = squad.player_name
        squad_dict["squad"] = squad.toDict()
        with open(self.loaded_file, 'w') as file:
            yaml.dump(squad_dict, file, sort_keys=False)
        
    @staticmethod
    def read_config_file(file: str = ''):
        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)
        else:
            base_path = Path(os.getcwd())
        config_file = base_path / "config" / file
        data = None
        with open(config_file, 'r') as file:
            data = yaml.safe_load(file)
        return data
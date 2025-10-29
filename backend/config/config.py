from backend.data_managers.file_manager import FileManager
from backend.models.ability import Ability
from backend.models.equipment import Equipment
from backend.models.mastery_power import MasteryPower
from backend.models.mastery import Mastery
from backend.models.upgrade import Upgrade
from backend.models.soldier_type import SoldierType

class Config():
    def __init__(self):
        self.ABILITIES: dict = None
        self.EQUIPMENT: dict = None
        self.MASTERIES: dict = None
        self.MASTERY_POWERS: dict = None
        self.SOLDIER_TYPES: dict = None
        self.UPGRADES: dict = None
        self.MAX_MASTERIES = 0
        self.MAX_PSYMANCERS = 0
        self.MAX_RARES = 0
        self.load_configs()
    
    def load_configs(self):
        MASTER_CONFIG = "master.yaml"
        master_data = self.load_config(MASTER_CONFIG)
        for data_type in master_data.keys():
            if data_type == "SquadRules":
                squad_rules = self.load_config(master_data["SquadRules"])
                for rule in squad_rules.keys():
                    setattr(self, rule.upper(), squad_rules[rule])
            else:
                config_file = master_data[data_type]
                attribute = config_file.split(".")[0].upper()
                data_config = self.load_config(config_file)
                attr_dict = {}
                target_class = globals()[data_type]
                for key in data_config.keys():
                    data_object = target_class.from_dict(key, data_config[key])
                    attr_dict[key] = data_object
                setattr(self, attribute, attr_dict)

    def load_config(self, file):
        return FileManager.read_config_file(file)
from backend.config.config import Config
from backend.models.squad import Squad
from backend.models.soldier import Soldier

class DataManager():
    def __init__(self):
        self.CONFIG = Config()
        self.LEADERSHIP_ABILITIES = {}
        self.GENERAL_ABILITIES = {}
        self.PSYMANCER_ABILITIES = {}
        self.PSYCHIC_POWERS = {}
        self.RANGED_WEAPONS = {}
        self.MELEE_WEAPONS = {}
        self.ITEMS = {}
        self.fillAbilityArrays()
        self.fillEquipmentArrays()
        self.squad = Squad()
        self.loaded_squad = Squad()

    def fillAbilityArrays(self):
        for name, upgrade in self.CONFIG.UPGRADES.items():
            if upgrade.type == "leadership":
                self.LEADERSHIP_ABILITIES[name] = upgrade
            elif upgrade.type == "general":
                self.GENERAL_ABILITIES[name] = upgrade
            elif upgrade.type == "psymancer":
                self.PSYMANCER_ABILITIES[name] = upgrade
            elif upgrade.type == "psychic_power":
                self.PSYCHIC_POWERS[name] = upgrade

    def fillEquipmentArrays(self):
        for name, item in self.CONFIG.EQUIPMENT.items():
            if item.type == "ranged":
                self.RANGED_WEAPONS[name] = item
            elif item.type == "melee":
                self.MELEE_WEAPONS[name] = item
            elif item.type == "item":
                self.ITEMS[name] = item

    def addSoldierToSquad(self, soldier):
        self.squad.addSoldier(soldier)

    def removeSoldier(self, soldier_index):
        self.squad.removeSoldier(soldier_index)

    def editSoldier(self, soldier_index, soldier):
        self.squad.replaceSoldier(soldier_index, soldier)

    def duplicateSoldier(self, soldier_index):
        self.squad.duplicateSoldier(soldier_index)

    def getSoldier(self, soldier_index):
        return self.squad.getSoldier(soldier_index)
    
    def addMasteryToSquad(self, mastery):
        self.squad.addMastery(self.CONFIG.MASTERIES[mastery])

    def newSquad(self):
        self.squad = Squad()

    def validateSquad(self):
        self.squad.validate(self)

    def squadChanged(self):
        return not self.loaded_squad == self.squad
    
    def loadSquad(self, file_data: dict = None):
        if not file_data:
            return
        squad = Squad()
        squad.player_name = file_data["player_name"]
        squad_data = file_data["squad"]
        squad.name = squad_data["name"]
        soldiers_data = squad_data["soldiers"]
        for soldier_data in soldiers_data:
            soldier = Soldier()
            soldier.name = soldier_data["name"]
            soldier.type = self.CONFIG.SOLDIER_TYPES[soldier_data["type"]]
            for upgrade in soldier_data["upgrades"]:
                soldier.upgrades.append(self.CONFIG.UPGRADES[upgrade])
            for equipment in soldier_data["equipment"]:
                soldier.equipment.append(self.CONFIG.EQUIPMENT[equipment])
            soldier.is_leader = soldier_data["is_leader"]
            soldier.leader_ability = (self.CONFIG.UPGRADES[soldier_data["leader_ability"]] 
                                      if soldier_data["leader_ability"] is not None else None)
            soldier.is_psymancer = soldier_data["is_psymancer"]
            soldier.psymancer_ability = (self.CONFIG.UPGRADES[soldier_data["psymancer_ability"]]
                                         if soldier_data["psymancer_ability"] is not None else None)
            for power in soldier_data["psychic_powers"]:
                soldier.psychic_powers.append(self.CONFIG.UPGRADES[power])
            squad.soldiers.append(soldier)
        masteries_data = squad_data["masteries"]
        for mastery in masteries_data:
            squad.masteries.append(self.CONFIG.MASTERIES[mastery])
        squad.leader = next((soldier for soldier in squad.soldiers if soldier.name == squad_data["leader"]), None)
        squad.psymancer = next((soldier for soldier in squad.soldiers if soldier.name == squad_data["psymancer"]), None)
        squad.wildcard = next((mastery for mastery in squad.masteries if mastery.name == squad_data["wildcard"]), None)
        squad.validate(self)
        self.squad = squad
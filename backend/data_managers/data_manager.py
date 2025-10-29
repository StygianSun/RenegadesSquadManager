from backend.config.config import Config
from backend.models.squad import Squad
from backend.models.soldier import Soldier
from backend.models.mastery import Mastery
from backend.models.mastery_power import MasteryPower
from backend.models.upgrade import Upgrade
from backend.models.equipment import Equipment
from backend.models.soldier_type import SoldierType

class DataManager():
    def __init__(self):
        self.CONFIG = Config()
        self.LEADERSHIP_ABILITIES: dict[str, Upgrade] = {}
        self.GENERAL_ABILITIES: dict[str, Upgrade] = {}
        self.PSYMANCER_ABILITIES: dict[str, Upgrade] = {}
        self.PSYCHIC_POWERS: dict[str, Upgrade] = {}
        self.RANGED_WEAPONS: dict[str, Equipment] = {}
        self.MELEE_WEAPONS: dict[str, Equipment] = {}
        self.ITEMS: dict[str, Equipment] = {}
        self.fillAbilityArrays()
        self.fillEquipmentArrays()
        self.squad = Squad()
        self.loaded_squad = Squad()

    def fillAbilityArrays(self):
        for name, upgrade in self.CONFIG.UPGRADES.items():
            if upgrade.upgrade_type == "leadership":
                self.LEADERSHIP_ABILITIES[name] = upgrade
            elif upgrade.upgrade_type == "general":
                self.GENERAL_ABILITIES[name] = upgrade
            elif upgrade.upgrade_type == "psymancer":
                self.PSYMANCER_ABILITIES[name] = upgrade
            elif upgrade.upgrade_type == "psychic_power":
                self.PSYCHIC_POWERS[name] = upgrade

    def fillEquipmentArrays(self):
        for name, item in self.CONFIG.EQUIPMENT.items():
            if item.type == "ranged":
                self.RANGED_WEAPONS[name] = item
            elif item.type == "melee":
                self.MELEE_WEAPONS[name] = item
            elif item.type == "item":
                self.ITEMS[name] = item

    def getLeadershipAbilityRules(self, leader_ability_name: str):
        return self.CONFIG.ABILITIES[leader_ability_name].rules
    
    def getMasteries(self) -> set[str]:
        return self.CONFIG.MASTERIES.keys()
    
    def getMastery(self, mastery_name: str) -> Mastery:
        return self.CONFIG.MASTERIES[mastery_name]
    
    def getAvailableMasteries(self) -> dict[str, bool]:
        available_masteries = {}
        for mastery_name, mastery in self.CONFIG.MASTERIES.items():
            if self.squad.wildcard is not None and mastery.type == self.squad.wildcard.type:
                available_masteries[mastery_name] = False
            else:
                available_masteries[mastery_name] = True
        return available_masteries
    
    def getPower(self, power_name: str) -> MasteryPower:
        return self.CONFIG.MASTERY_POWERS[power_name]
    
    def getPsymancerPowerCount(self, psymancer_grade: str) -> int:
        return self.PSYMANCER_ABILITIES[psymancer_grade].modifications["psychic_powers"]
    
    def getDefaultSoldierType(self) -> SoldierType:
        return SoldierType()
    
    def applyTypeToSoldier(self, soldier: Soldier, soldier_type: SoldierType):
        soldier.soldier_type = soldier_type
        soldier.vitality = soldier_type.vitality
        soldier.max_slots = soldier_type.max_slots
        soldier.ap = soldier_type.ap
        soldier.base_move = soldier_type.base_move
        soldier.dash_move = soldier_type.dash_move
        soldier.move_type = soldier_type.move_type
        soldier.abilities = [self.CONFIG.ABILITIES[ability] for ability in soldier_type.abilities]
        soldier.cost = soldier_type.cost
        soldier.rares_allowed = soldier_type.rares_allowed

    def getFormattedUpgrade(self, upgrade_name: str) -> dict[str, str | int | list[str]]:
        upgrade = self.CONFIG.UPGRADES[upgrade_name]
        rarity = ""
        if upgrade.is_rare:
            rarity = self.asStars(upgrade.rare_cost)
        return {
            "cost": upgrade.cost,
            "rarity": rarity,
            "has_options": upgrade.has_options
        }

    def applySoldierUpgrade(self, soldier: Soldier, upgrade_name: str):
        upgrade = self.CONFIG.UPGRADES[upgrade_name]
        soldier.upgrades.append(upgrade)
        soldier.validate(self)
    
    def unapplySoldierUpgrade(self, soldier: Soldier, upgrade_name: str):
        upgrade = self.CONFIG.UPGRADES[upgrade_name]
        soldier.upgrades.remove(upgrade)
        soldier.validate(self)

    def getAllowedEquipmentForSoldierType(self, soldier_type: SoldierType) -> dict[str, bool]:
        allowed_equipment = {}
        allowed_equipment["rares"] = soldier_type.rares_allowed
        allowed_equipment["items"] = soldier_type.items_allowed
        allowed_equipment["equipment"] = soldier_type.equipment_allowed
        allowed_equipment["melee"] = soldier_type.melee_allowed
        return allowed_equipment
    
    def getIsEquipmentRare(self) -> dict[str, bool]:
        equipment_is_rare = {}
        for name, equipment in self.CONFIG.EQUIPMENT.items():
            equipment_is_rare[name] = equipment.is_rare
        return equipment_is_rare
    
    def setSoldierAsLeader(self, soldier: Soldier, ability_name: str):
        soldier.is_leader = True
        soldier.leader_ability = self.CONFIG.UPGRADES[ability_name]
        for ability in soldier.leader_ability.abilities:
            soldier.abilities.append(self.CONFIG.ABILITIES[ability])
        soldier.cost += (soldier.vitality * soldier.leader_ability.cost)

    def unsetSoldierAsLeader(self, soldier: Soldier):
        soldier.is_leader = False
        soldier.cost -= (soldier.vitality * soldier.leader_ability.cost)
        for ability in soldier.leader_ability.abilities:
            soldier.abilities.remove(self.CONFIG.ABILITIES[ability])
        soldier.leader_ability = None

    def setSoldierAsPsymancer(self, soldier: Soldier, psychic_powers: list[str]):
        soldier.psymancer_ability = self.CONFIG.UPGRADES[psychic_powers[0]]
        for ability in soldier.psymancer_ability.abilities:
            soldier.abilities.append(self.CONFIG.ABILITIES[ability])
        for power in psychic_powers[1:]:
            if power != " ":
                soldier.psychic_powers.append(self.CONFIG.UPGRADES[power])
        for power in soldier.psychic_powers:
            for ability in power.abilities:
                soldier.abilities.append(self.CONFIG.ABILITIES[ability])
        soldier.is_psymancer = True
        soldier.cost += (soldier.vitality * soldier.psymancer_ability.cost)

    def unsetSoldierAsPsymancer(self, soldier: Soldier):
        soldier.is_psymancer = False
        soldier.cost -= (soldier.vitality * soldier.psymancer_ability.cost)
        for power in soldier.psychic_powers:
            for ability in power.abilities:
                soldier.abilities.remove(self.CONFIG.ABILITIES[ability])
        soldier.psychic_powers = []
        for ability in soldier.psymancer_ability.abilities:
            soldier.abilities.remove(self.CONFIG.ABILITIES[ability])
        soldier.psymancer_ability = None

    def getSquadMembersAsRows(self) -> dict[str, dict[str, str | list[str]]]:
        squad_rows = {}
        for soldier in self.squad.soldiers:
            squad_rows[soldier.name] = {
                "type": soldier.soldier_type.name,
                "is_leader": "Yes" if soldier.is_leader else "",
                "is_psymancer": "Yes" + soldier.psymancer_ability.name if soldier.is_psymancer else "",
                "cost": str(soldier.cost),
                "upgrades": [upgrade.name for upgrade in soldier.upgrades],
                "equipment": [equipment.name for equipment in soldier.equipment]
            }
        return squad_rows
    
    def getRaresInSquad(self) -> dict[str, str]:
        rares_list = {}
        for soldier in self.squad.soldiers:
            if soldier.soldier_type.is_rare:
                rares_list[soldier.soldier_type.name] = self.asStars(soldier.soldier_type.rare_cost)
            for upgrade in soldier.upgrades:
                if upgrade.is_rare:
                    rares_list[upgrade.name] = self.asStars(upgrade.rare_cost)
            for equipment in soldier.equipment:
                if equipment.is_rare:
                    rares_list[equipment.name] = self.asStars(equipment.rare_cost)
        return rares_list

    def asStars(self, rare_cost: int) -> str:
        rarity = ""
        for _ in range(rare_cost):
            rarity += u'\u2605' # Unicode star character
        return rarity
    
    def getSquadMasteriesAsRows(self) -> dict[str, dict[str, str | list[str]]]:
        mastery_rows = {}
        for mastery in self.squad.masteries:
            mastery_rows[mastery.name] = {
                "type": mastery.type,
                "powers": [power for power in mastery.powers]
            }
        return mastery_rows

    def squadCost(self) -> int:
        squad_cost = 0
        for soldier in self.squad.soldiers:
            squad_cost += soldier.cost
        return squad_cost
    
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
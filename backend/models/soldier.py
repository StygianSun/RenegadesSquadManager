from backend.models.soldier_type import SoldierType
from backend.models.upgrade import Upgrade
from backend.models.equipment import Equipment
from backend.models.ability import Ability

class Soldier():
    def __init__(self, name: str = '', type: SoldierType = None, vitality: int = 0, max_slots: int = 0, cur_slots: int = 0,
                 ap: int = 0, base_move: int = 0, dash_move: str = 'D0', move_type: list[str] = ['Normal'], 
                 upgrades: list[Upgrade] = None, equipment: list[Equipment] = None, rares_allowed: bool = False,
                 is_leader: bool = False, is_psymancer: bool = False):
        self.name: str = name
        self.type: SoldierType = type
        self.vitality: int = vitality
        self.max_slots: int = max_slots
        self.cur_slots: int = cur_slots
        self.ap: int = ap
        self.base_move: int = base_move
        self.dash_move: str = dash_move
        self.move_type: list[str] = move_type
        self.upgrades: list[Upgrade] = upgrades if upgrades is not None else []
        self.equipment: list[Equipment] = equipment if equipment is not None else []
        self.rares_allowed: bool = rares_allowed
        self.is_leader: bool = is_leader
        self.leader_ability: Upgrade = None
        self.is_psymancer: bool = is_psymancer
        self.psymancer_ability: Upgrade = None
        self.psychic_powers: list[Upgrade] = []
        self.cost = 0
        self.abilities: list[Ability] = []

    def validateCost(self):
        try:
            self.cost = self.type.cost
            for upgrade in self.upgrades:
                self.cost += upgrade.cost
            if self.is_leader:
                self.cost += (self.vitality * self.leader_ability.cost)
            if self.is_psymancer:
                self.cost += (self.vitality * self.psymancer_ability.cost)
            for item in self.equipment:
                self.cost += item.cost
        except:
            #Do nothing
            print("Cost validation failed")

    def validateType(self, data_manager):
        try:
            self.vitality = self.type.vitality
            self.max_slots = self.type.max_slots
            self.ap = self.type.ap
            self.base_move = self.type.base_move
            self.dash_move = self.type.dash_move
            self.move_type = self.type.move_type
            self.abilities = [data_manager.CONFIG.ABILITIES[ability] for ability in self.type.abilities]
            self.cost = self.type.cost
            self.rares_allowed = self.type.rares_allowed
        except:
            #Do Nothing
            print("Type validation failed")

    def validateUpgrades(self, data_manager):
        try:
            for upgrade in self.upgrades:
                self.abilities.extend(data_manager.CONFIG.ABILITIES[ability] for ability in upgrade.abilities)
                for modification in upgrade.modifications:
                    if modification in ["weapon_type", "equipment", "weapon"]:
                        pass #Handle non-standard mods
                    else:
                        if upgrade.modifications[modification]["mod"] == "add":
                            setattr(self, modification, getattr(self, modification) + 
                                upgrade.modifications[modification]["value"])
                        elif upgrade.modifications[modification]["mod"] == "equals":
                            setattr(self, modification, upgrade.modifications[modification]["value"])
        except:
            #Do nothing
            print("Upgrade validation failed")

    def validateEquipment(self):
        try:
            self.cur_slots = 0
            for item in self.equipment:
                self.cur_slots += item.slots
        except:
            #Do nothing
            print("Equipment validation failed")
            pass

    def validateLeader(self, data_manager):
        try:
            if self.is_leader and self.leader_ability is not None:
                for ability in self.leader_ability.abilities:
                    self.abilities.append(data_manager.CONFIG.ABILITIES[ability])
        except:
            #Do nothing
            print("Leader validation failed")

    def validatePsymancer(self, data_manager):
        try:
            if self.is_psymancer and self.psymancer_ability is not None:
                for ability in self.psymancer_ability.abilities:
                    self.abilities.append(data_manager.CONFIG.ABILITIES[ability])
                for power in self.psychic_powers:
                    for ability in power.abilities:
                        self.abilities.append(data_manager.CONFIG.ABILITIES[ability])
        except:
            #Do nothing
            print("Psymancer validation failed")

    def validate(self, data_manager):
        try:
            self.validateType(data_manager)
            self.validateEquipment()
            self.validateUpgrades(data_manager)
            self.validateLeader(data_manager)
            self.validatePsymancer(data_manager)
            self.validateCost()
        except:
            # Do Nothing
            print("Full validation failed")
            pass

    def __repr__(self):
        return f"""Soldier(name='{self.name}', type='{self.type}', vitality='{self.vitality}',
            max_slots='{self.max_slots}', ap='{self.ap}', base_move='{self.base_move}',
            dash_move='{self.dash_move}', move_type='{self.move_type}', abilities='{self.abilities}',
            upgrades='{self.upgrades}', cost='{self.cost}', equipment='{self.equipment}',
            is_leader='{self.is_leader}', is_psymancer='{self.is_psymancer}',
            leader_ability='{self.leader_ability}', psymancer_ability='{self.psymancer_ability}',
            psychic_powers='{self.psychic_powers}', rares_allowed='{self.rares_allowed}'"""
    
    def __eq__(self, other):
        return (
            isinstance(other, Soldier) and
            self.name == other.name and
            self.type == other.type and
            self.vitality == other.vitality and
            self.max_slots == other.max_slots and
            self.cur_slots == other.cur_slots and
            self.ap == other.ap and
            self.base_move == other.base_move and
            self.dash_move == other.dash_move and
            self.move_type == other.move_type and
            self.upgrades == other.upgrades and
            self.equipment == other.equipment and
            self.rares_allowed == other.rares_allowed and
            self.is_leader == other.is_leader and
            self.leader_ability == other.leader_ability and
            self.is_psymancer == other.is_psymancer and
            self.psymancer_ability == other.psymancer_ability and
            self.psychic_powers == other.psychic_powers and
            self.cost == other.cost and
            self.abilities == other.abilities
        )
    
    def toDict(self):
        soldier_dict = {}
        soldier_dict["name"] = self.name
        soldier_dict["type"] = self.type.name
        soldier_dict["upgrades"] = [upgrade.name for upgrade in self.upgrades]
        soldier_dict["equipment"] = [equipment.name for equipment in self.equipment]
        soldier_dict["is_leader"] = self.is_leader
        soldier_dict["leader_ability"] = self.leader_ability.name if self.leader_ability is not None else None
        soldier_dict["is_psymancer"] = self.is_psymancer
        soldier_dict["psymancer_ability"] = self.psymancer_ability.name if self.psymancer_ability is not None else None
        soldier_dict["psychic_powers"] = [power.name for power in self.psychic_powers]
        return soldier_dict
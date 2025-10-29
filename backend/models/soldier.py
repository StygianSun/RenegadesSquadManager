from typing import Optional, List

from backend.models.soldier_type import SoldierType
from backend.models.upgrade import Upgrade
from backend.models.equipment import Equipment
from backend.models.ability import Ability
import logging
import traceback

logger = logging.getLogger(__name__)

# Module-level cached Config singleton used when callers don't provide a DataManager
_SOLDIER_CONFIG = None

def _get_config():
    """Lazily import and return a cached Config instance to avoid circular imports.

    When callers pass a DataManager, its CONFIG is used. When callers omit it,
    this function will import Config locally and cache an instance.
    """
    global _SOLDIER_CONFIG
    if _SOLDIER_CONFIG is None:
        from backend.config.config import Config
        _SOLDIER_CONFIG = Config()
    return _SOLDIER_CONFIG

class Soldier():

    def __init__(self, name: str = '', soldier_type: Optional[SoldierType] = None, vitality: int = 0, max_slots: int = 0, cur_slots: int = 0,
                 ap: int = 0, base_move: int = 0, dash_move: str = 'D0', move_type: Optional[List[str]] = None, 
                 upgrades: Optional[List[Upgrade]] = None, equipment: Optional[List[Equipment]] = None, rares_allowed: bool = False,
                 is_leader: bool = False, is_psymancer: bool = False):
        self.name: str = name
        self.soldier_type: Optional[SoldierType] = soldier_type
        self.vitality: int = vitality
        self.max_slots: int = max_slots
        self.cur_slots: int = cur_slots
        self.ap: int = ap
        self.base_move: int = base_move
        self.dash_move: str = dash_move
        self.move_type: List[str] = move_type if move_type is not None else ['Normal']
        self.upgrades: List[Upgrade] = upgrades if upgrades is not None else []
        self.equipment: List[Equipment] = equipment if equipment is not None else []
        self.rares_allowed: bool = rares_allowed
        self.is_leader: bool = is_leader
        self.leader_ability: Optional[Upgrade] = None
        self.is_psymancer: bool = is_psymancer
        self.psymancer_ability: Optional[Upgrade] = None
        self.psychic_powers: List[Upgrade] = []
        self.cost = 0
        self.abilities: List[Ability] = []

    def validateCost(self):
        try:
            if self.soldier_type is None:
                raise ValueError("Soldier has no soldier_type set")
            self.cost = self.soldier_type.cost
            for upgrade in self.upgrades:
                self.cost += upgrade.cost
            if self.is_leader and self.leader_ability is not None:
                self.cost += (self.vitality * self.leader_ability.cost)
            if self.is_psymancer and self.psymancer_ability is not None:
                self.cost += (self.vitality * self.psymancer_ability.cost)
            for item in self.equipment:
                if isinstance(item.cost, str):
                    self.cost += int(item.cost[0]) * self.vitality
                else:
                    self.cost += item.cost
        except Exception as e:
            logger.exception("Cost validation failed: %s", e)
            raise e

    def validateType(self, data_manager):
        try:
            if self.soldier_type is None:
                raise ValueError("Soldier has no soldier_type set")
            # Allow callers to omit a DataManager by using a cached Config singleton
            cfg = data_manager.CONFIG if data_manager is not None else _get_config()
            self.vitality = self.soldier_type.vitality
            self.max_slots = self.soldier_type.max_slots
            self.ap = self.soldier_type.ap
            self.base_move = self.soldier_type.base_move
            self.dash_move = self.soldier_type.dash_move
            self.move_type = self.soldier_type.move_type
            self.abilities = [cfg.ABILITIES[ability] for ability in self.soldier_type.abilities]
            self.cost = self.soldier_type.cost
            self.rares_allowed = self.soldier_type.rares_allowed
        except Exception as e:
            logger.exception("Type validation failed: %s", e)
            raise e

    def validateUpgrades(self, data_manager):
        try:
            cfg = data_manager.CONFIG if data_manager is not None else _get_config()
            for upgrade in self.upgrades:
                self.abilities.extend(cfg.ABILITIES[ability] for ability in upgrade.abilities)
                for modification in upgrade.modifications:
                    if modification in ["weapon_type", "equipment", "weapon"]:
                        pass #Handle non-standard mods
                    else:
                        if upgrade.modifications[modification]["mod"] == "add":
                            setattr(self, modification, getattr(self, modification) + 
                                upgrade.modifications[modification]["value"])
                        elif upgrade.modifications[modification]["mod"] == "equals":
                            setattr(self, modification, upgrade.modifications[modification]["value"])
        except Exception as e:
            logger.exception("Upgrade validation failed: %s", e)
            raise e

    def validateEquipment(self):
        try:
            self.cur_slots = 0
            for item in self.equipment:
                self.cur_slots += item.slots
        except Exception as e:
            logger.exception("Equipment validation failed: %s", e)
            raise e

    def validateLeader(self, data_manager):
        try:
            if self.is_leader and self.leader_ability is not None:
                cfg = data_manager.CONFIG if data_manager is not None else _get_config()
                for ability in self.leader_ability.abilities:
                    self.abilities.append(cfg.ABILITIES[ability])
        except Exception as e:
            logger.exception("Leader validation failed: %s", e)
            raise e

    def validatePsymancer(self, data_manager):
        try:
            if self.is_psymancer and self.psymancer_ability is not None:
                cfg = data_manager.CONFIG if data_manager is not None else _get_config()
                for ability in self.psymancer_ability.abilities:
                    self.abilities.append(cfg.ABILITIES[ability])
                for power in self.psychic_powers:
                    for ability in power.abilities:
                        self.abilities.append(cfg.ABILITIES[ability])
        except Exception as e:
            logger.exception("Psymancer validation failed: %s", e)
            raise e

    def validate(self, data_manager=None):
        try:
            self.validateType(data_manager)
            self.validateEquipment()
            self.validateUpgrades(data_manager)
            self.validateLeader(data_manager)
            self.validatePsymancer(data_manager)
            self.validateCost()
        except Exception as e:
            logger.exception("Full validation failed: %s", e)
            raise e
        
    def getDisplayTexts(self) -> dict[str, str]:
        rarity = ""
        abilities = ""
        if self.soldier_type is not None:
            if self.soldier_type.is_rare:
                for _ in range(self.soldier_type.rare_cost):
                    rarity += u'\u2605' # Unicode star character
            abilities += ", ".join(ability.name for ability in self.abilities)
        return {
            "cost": str(self.cost),
            "vitality": str(self.vitality),
            "slots": str(self.cur_slots) + "/" + str(self.max_slots),
            "ap": str(self.ap),
            "move": (str(self.base_move) + "\" + " + self.dash_move + " " + ", ".join(self.move_type)),
            "rarity": rarity,
            "abilities": abilities,
            "leader_ability": self.leader_ability.name if self.leader_ability is not None else "",
            "psymancer_ability": self.psymancer_ability.name if self.psymancer_ability is not None else "",
            "psychic_powers": ", ".join(power.name for power in self.psychic_powers)
        }

    def __repr__(self):
        return f"""Soldier(name='{self.name}', type='{self.soldier_type}', vitality='{self.vitality}',
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
            self.soldier_type == other.soldier_type and
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
        soldier_dict["type"] = self.soldier_type.name if self.soldier_type is not None else None
        soldier_dict["upgrades"] = [upgrade.name for upgrade in self.upgrades]
        soldier_dict["equipment"] = [equipment.name for equipment in self.equipment]
        soldier_dict["is_leader"] = self.is_leader
        soldier_dict["leader_ability"] = self.leader_ability.name if self.leader_ability is not None else None
        soldier_dict["is_psymancer"] = self.is_psymancer
        soldier_dict["psymancer_ability"] = self.psymancer_ability.name if self.psymancer_ability is not None else None
        soldier_dict["psychic_powers"] = [power.name for power in self.psychic_powers]
        return soldier_dict
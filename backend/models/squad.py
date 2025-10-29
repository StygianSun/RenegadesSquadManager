from backend.models.soldier import Soldier
from backend.models.mastery import Mastery

class Squad():
    def __init__(self, player_name: str = '', name: str = '', soldiers: list[Soldier] = None, masteries: list[Mastery] = None):
        self.player_name: str = player_name
        self.name: str = name
        self.soldiers: list[Soldier] = soldiers if soldiers is not None else []
        self.masteries: list[Mastery] = masteries if masteries is not None else []
        self.leader = next((soldier for soldier in self.soldiers if soldier.is_leader), None)
        self.psymancer = next((soldier for soldier in self.soldiers if soldier.is_psymancer), None)
        self.wildcard = next((mastery for mastery in self.masteries if mastery.only_one_of_type), None)

    def isEmpty(self):
        return (self.name == '' and len(self.soldiers) == 0 and len(self.masteries) == 0 and
            self.leader is None and self.psymancer is None and self.wildcard is None)

    def hasLeader(self):
        return True if self.leader else False
    
    def hasPsymancer(self):
        return True if self.psymancer else False
    
    def addSoldier(self, soldier):
        self.soldiers.append(soldier)
        if soldier.is_leader and self.leader == None:
            self.leader = soldier
        if soldier.is_psymancer and self.psymancer == None:
            self.psymancer = soldier

    def removeSoldier(self, soldier_index):
        soldier = self.soldiers[soldier_index]
        if soldier.is_leader and self.leader != None:
            self.leader = None
        if soldier.is_psymancer and self.psymancer != None:
            self.psymancer = None
        self.soldiers.pop(soldier_index)

    def replaceSoldier(self, soldier_index, soldier):
        if soldier.is_leader and self.leader != soldier:
            self.leader = soldier
        if soldier.is_psymancer and self.psymancer != soldier:
            self.psymancer = soldier
        self.soldiers[soldier_index] = soldier

    def duplicateSoldier(self, soldier_index):
        soldier_to_duplicate = self.soldiers[soldier_index]
        if not soldier_to_duplicate.is_leader and not soldier_to_duplicate.is_psymancer:
            duped_soldier = Soldier(soldier_to_duplicate.name,
                                    soldier_to_duplicate.type,
                                    soldier_to_duplicate.vitality,
                                    soldier_to_duplicate.max_slots,
                                    soldier_to_duplicate.cur_slots,
                                    soldier_to_duplicate.ap,
                                    soldier_to_duplicate.base_move,
                                    soldier_to_duplicate.dash_move,
                                    soldier_to_duplicate.move_type,
                                    soldier_to_duplicate.upgrades,
                                    soldier_to_duplicate.equipment,
                                    soldier_to_duplicate.rares_allowed,
                                    soldier_to_duplicate.is_leader,
                                    soldier_to_duplicate.is_psymancer)
            duped_soldier.validate()
            self.soldiers.append(duped_soldier)

    def getSoldier(self, soldier_index):
        return self.soldiers[soldier_index]
    
    def addMastery(self, mastery):
        self.masteries.append(mastery)
        if mastery.only_one_of_type and self.wildcard is None:
            self.wildcard = mastery

    def validate(self, data_manager):
        cost = 0
        for soldier in self.soldiers:
            cost += soldier.cost
        valid_masteries = len(self.masteries) <= data_manager.CONFIG.MAX_MASTERIES
        total_rare_cost = 0
        for soldier in self.soldiers:
            soldier.validate(data_manager)
            if soldier.soldier_type.is_rare:
                total_rare_cost += soldier.soldier_type.rare_cost
            for upgrade in soldier.upgrades:
                if upgrade.is_rare:
                    total_rare_cost += upgrade.rare_cost
            for equipment in soldier.equipment:
                if equipment.is_rare:
                    total_rare_cost += equipment.rare_cost
        valid_rares = total_rare_cost <= data_manager.CONFIG.MAX_RARES
        valid_psymancers = type(self.psymancer) != list
        return [cost, valid_masteries, valid_rares, valid_psymancers]

    def __eq__(self, other: object) -> bool:
        return(
            isinstance(other, Squad) and
            self.name == other.name and
            self.soldiers == other.soldiers and
            self.masteries == other.masteries and
            self.leader == other.leader and
            self.psymancer == other.psymancer and
            self.wildcard == other.wildcard
        )
    
    def toDict(self):
        squad_dict = {}
        squad_dict["name"] = self.name
        squad_dict["soldiers"] = []
        for soldier in self.soldiers:
            squad_dict["soldiers"].append(soldier.toDict())
        squad_dict["masteries"] = []
        for mastery in self.masteries:
            squad_dict["masteries"].append(mastery.name)
        squad_dict["leader"] = self.leader.name if self.leader is not None else None
        squad_dict["psymancer"] = self.psymancer.name if self.psymancer is not None else None
        squad_dict["wildcard"] = self.wildcard.name if self.wildcard is not None else None
        return squad_dict
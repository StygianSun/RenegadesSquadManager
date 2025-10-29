

class MasteryPower():
    def __init__(self, name: str = '', is_epic: bool = False, is_passive: bool = False, sp_cost: str = '',
                 rules: str = ''):
        self.name: str = name
        self.is_epic: bool = is_epic
        self.is_passive: bool = is_passive
        self.sp_cost: str = sp_cost
        self.rules: str = rules

    @classmethod
    def from_dict(cls, name: str = '', rules_dict: dict = None):
        is_epic = rules_dict["is_epic"]
        is_passive = rules_dict["is_passive"]
        sp_cost = rules_dict["sp_cost"]
        rules = rules_dict["rules"]
        return cls(name, is_epic, is_passive, sp_cost, rules)
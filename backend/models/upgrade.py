

class Upgrade():
    def __init__(self, name: str = '', type: str = '', cost: int = 0, is_rare: bool = False, rare_cost: int = 0,
                 has_options: list[str] = [], abilities: list[str] = [], modifications: dict = {}):
        self.name: str = name
        self.type: str = type
        self.cost: int = cost
        self.is_rare: bool = is_rare
        self.rare_cost: int = rare_cost
        self.has_options: list[str] = has_options
        self.abilities: list[str] = abilities
        self.modifications: dict = modifications

    @classmethod
    def from_dict(cls, name: str = '', rules_dict: dict = None):
        type = rules_dict["type"]
        cost = rules_dict["cost"]
        is_rare = rules_dict["is_rare"]
        rare_cost = rules_dict["rare_cost"]
        has_options = rules_dict["has_options"]
        abilities = rules_dict["abilities"]
        modifications = rules_dict["modifications"]
        return cls(name, type, cost, is_rare, rare_cost, has_options, abilities, modifications)
    
    def __eq__(self, other):
        return (
            isinstance(other, Upgrade) and
            self.name == other.name and
            self.type == other.type and
            self.is_rare == other.is_rare and
            self.rare_cost == other.rare_cost and
            self.has_options == other.has_options and
            self.abilities == other.abilities and
            self.modifications == other.modifications
        )
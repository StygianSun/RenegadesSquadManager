

class Upgrade():
    def __init__(self, name: str = '', upgrade_type: str = '', cost: int = 0, is_rare: bool = False, rare_cost: int = 0,
                 has_options: list[str] = None, abilities: list[str] = None, modifications: dict = None):
        self.name: str = name
        self.upgrade_type: str = upgrade_type
        self.cost: int = cost
        self.is_rare: bool = is_rare
        self.rare_cost: int = rare_cost
        self.has_options: list[str] = has_options if has_options is not None else []
        self.abilities: list[str] = abilities if abilities is not None else []
        self.modifications: dict = modifications if modifications is not None else {}

    @classmethod
    def from_dict(cls, name: str = '', rules_dict: dict = None):
        upgrade_type = rules_dict["type"]
        cost = rules_dict["cost"]
        is_rare = rules_dict["is_rare"]
        rare_cost = rules_dict["rare_cost"]
        has_options = rules_dict["has_options"]
        abilities = rules_dict["abilities"]
        modifications = rules_dict["modifications"]
        return cls(name, upgrade_type, cost, is_rare, rare_cost, has_options, abilities, modifications)
    
    def __eq__(self, other):
        return (
            isinstance(other, Upgrade) and
            self.name == other.name and
            self.upgrade_type == other.upgrade_type and
            self.is_rare == other.is_rare and
            self.rare_cost == other.rare_cost and
            self.has_options == other.has_options and
            self.abilities == other.abilities and
            self.modifications == other.modifications
        )
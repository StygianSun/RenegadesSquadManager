

class Equipment():
    def __init__(self, name: str = '', cost: str = '0', slots: int = 0, range: int = 0, attack_dice: int = 0,
                dmg: int = 0, special_rules: list[str] = [], type: str = '', rules: str = '', is_rare: bool = False,
                rare_cost: int = 0):
        self.name: str = name
        self.cost: str = cost
        self.slots: int = slots
        self.range: int = range
        self.attack_dice: int = attack_dice
        self.dmg: int = dmg
        self.special_rules: list[str] = special_rules
        self.type: str = type
        self.rules: str = rules
        self.is_rare: bool = is_rare
        self.rare_cost: int = rare_cost

    @classmethod
    def from_dict(cls, name: str = '', rules_dict: dict = None):
        cost = rules_dict["cost"]
        slots = rules_dict["slots"]
        range = rules_dict["range"]
        attack_dice = rules_dict["attack_dice"]
        dmg = rules_dict["dmg"]
        special_rules = rules_dict["special_rules"]
        type = rules_dict["type"]
        rules = rules_dict["rules"]
        is_rare = rules_dict["is_rare"]
        rare_cost = rules_dict["rare_cost"]
        return cls(name, cost, slots, range, attack_dice, dmg, special_rules,
                   type, rules, is_rare, rare_cost)
    
    def toFormattedDict(self) -> dict[str, str]:
        rarity = ""
        if self.is_rare:
            for _ in range(self.rare_cost):
                rarity += u'\u2605' # Unicode star character
        if self.range == -1:
            range_text = "Long (" + u'\u221E' + ")"
        elif self.range == 18:
            range_text = "Medium (18\")"
        elif self.range == 12:
            range_text = "Short (12\")"
        elif self.range == 1:
            range_text = "Melee (1\")"
        elif self.range == 0:
            range_text = "-"
        else:
            range_text = str(self.range) + "\""
        atk_text = str(self.attack_dice) if self.attack_dice != 0 else "-"
        dmg_text = str(self.dmg) if self.dmg != 0 else "-"
        return {
            "name": self.name,
            "cost": str(self.cost),
            "rarity": rarity,
            "range": range_text,
            "atk_dice": atk_text,
            "dmg": dmg_text
        }
    
    def __eq__(self, other):
        return (
            isinstance(other, Equipment) and
            self.name == other.name and
            self.cost == other.cost and
            self.slots == other.slots and
            self.range == other.range and
            self.attack_dice == other.attack_dice and
            self.dmg == other.dmg and
            self.special_rules == other.special_rules and
            self.type == other.type and
            self.rules == other.rules and
            self.is_rare == other.is_rare and
            self.rare_cost == other.rare_cost
        )
class SoldierType():
    def __init__(self, name: str = '', vitality: int = 0, max_slots: int = 0, ap: int = 0, base_move: int = 0,
                 dash_move: str = 'D0', move_type: list[str] = ['Normal'], abilities: list[str] = [],
                 upgrades: list[str] = [], cost: int = 0, is_rare: bool = False, rare_cost: int = 0,
                 rares_allowed: bool = False, items_allowed: bool = False, equipment_allowed: bool = False,
                 melee_allowed: bool = False):
        self.name: str = name
        self.vitality: int = vitality
        self.max_slots: int = max_slots
        self.ap: int = ap
        self.base_move: int = base_move
        self.dash_move: str = dash_move
        self.move_type: list[str] = move_type
        self.abilities: list[str] = abilities
        self.upgrades: list[str] = upgrades
        self.cost: int = cost
        self.is_rare: bool = is_rare
        self.rare_cost: int = rare_cost
        self.rares_allowed: bool = rares_allowed
        self.items_allowed: bool = items_allowed
        self.equipment_allowed: bool = equipment_allowed
        self.melee_allowed: bool = melee_allowed

    @classmethod
    def from_dict(cls, name: str = '', rules_dict: dict = None):
        vitality = rules_dict["vitality"]
        max_slots = rules_dict["max_slots"]
        ap = rules_dict["ap"]
        base_move = rules_dict["base_move"]
        dash_move = rules_dict["dash_move"]
        move_type = rules_dict["move_type"]
        abilities = rules_dict["abilities"]
        upgrades = rules_dict["upgrades"]
        cost = rules_dict["cost"]
        is_rare = rules_dict["is_rare"]
        rare_cost = rules_dict["rare_cost"]
        rares_allowed = rules_dict["rares_allowed"]
        items_allowed = rules_dict["items_allowed"]
        equipment_allowed = rules_dict["equipment_allowed"]
        melee_allowed = rules_dict["melee_allowed"]
        return cls(name, vitality, max_slots, ap, base_move, dash_move, move_type, abilities,
                   upgrades, cost, is_rare, rare_cost, rares_allowed, items_allowed, equipment_allowed,
                   melee_allowed)
    
    def __repr__(self):
        return f"""SoldierType(name='{self.name}', vitality='{self.vitality}', max_slots='{self.max_slots}',
            ap='{self.ap}', base_move='{self.base_move}', dash_move='{self.dash_move}', move_type='
            {self.dash_move}', abilities='{self.abilities}', upgrades='{self.upgrades}', cost='{self.cost}',
            is_rare='{self.is_rare}', rare_cost='{self.rare_cost}', rares_allowed='{self.rares_allowed}',
            items_allowed='{self.items_allowed}', equipment_allowed='{self.equipment_allowed}',
            melee_allowed='{self.melee_allowed}')"""
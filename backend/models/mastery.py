class Mastery():
    def __init__(self, name: str = '', type: str = '', powers: list[str] = [], only_one_of_type: bool = False):
        self.name: str = name
        self.type: str = type
        self.powers: list[str] = powers
        self.only_one_of_type: bool = only_one_of_type

    @classmethod
    def from_dict(cls, name: str = '', rules_dict: dict = ''):
        type = rules_dict["type"]
        powers = rules_dict["powers"]
        only_one_of_type = rules_dict["only_one_of_type"]
        return cls(name, type, powers, only_one_of_type)
    
    def __eq__(self, other):
        return (
            isinstance(other, Mastery) and
            self.name == other.name and
            self.type == other.type and
            self.powers == other.powers and
            self.only_one_of_type == other.only_one_of_type
        )
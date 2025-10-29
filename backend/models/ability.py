
class Ability():
    def __init__(self, name: str = '', rules: str = ''):
        self.name: str = name
        self.rules: str = rules

    @classmethod
    def from_dict(cls, name: str = '', rules: str = ''):
        return cls(name, rules)
    
    def __eq__(self, other):
        return (
            isinstance(other, Ability) and
            self.name == other.name and
            self.rules == other.rules
        )
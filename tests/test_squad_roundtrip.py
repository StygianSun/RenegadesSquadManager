from backend.models.squad import Squad
from backend.models.soldier import Soldier
from backend.models.soldier_type import SoldierType


def test_squad_toDict_basic_structure():
    st = SoldierType(name="Grunt", vitality=3, max_slots=2, ap=2, base_move=3, dash_move='D0', move_type=['Normal'], abilities=[], upgrades=[], cost=10)
    s = Soldier(name="Kade", soldier_type=st, vitality=3)
    squad = Squad(player_name="Alice", name="Strike Team")
    squad.soldiers.append(s)

    d = squad.toDict()
    assert isinstance(d, dict)
    assert d["name"] == "Strike Team"
    assert isinstance(d["soldiers"], list)
    assert len(d["soldiers"]) == 1
    soldier_d = d["soldiers"][0]
    assert soldier_d["name"] == "Kade"
    assert soldier_d["type"] == "Grunt"
    assert soldier_d["upgrades"] == []
    assert soldier_d["equipment"] == []
    assert soldier_d["is_leader"] is False
    assert soldier_d["leader_ability"] is None
    assert d["masteries"] == []
    assert d["leader"] is None
    assert d["psymancer"] is None
    assert d["wildcard"] is None

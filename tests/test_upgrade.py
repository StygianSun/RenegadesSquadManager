import yaml
from pathlib import Path

from backend.models.upgrade import Upgrade


def test_upgrade_from_dict_matches_yaml():
    repo_root = Path.cwd()
    config_path = repo_root / "backend" / "config" / "rules_configurations" / "upgrades.yaml"
    assert config_path.exists(), f"expected upgrades.yaml at {config_path}"
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # pick the first upgrade in the YAML and construct an Upgrade
    key = next(iter(data.keys()))
    rules = data[key]

    up = Upgrade.from_dict(key, rules)

    # Basic assertions that mapping occurred
    assert up.name == key
    assert hasattr(up, "upgrade_type")
    assert hasattr(up, "cost")
    assert isinstance(up.cost, int)
    assert isinstance(up.is_rare, bool)
    assert isinstance(up.has_options, list)
    assert isinstance(up.abilities, list)

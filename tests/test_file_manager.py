from backend.data_managers.file_manager import FileManager
from pathlib import Path


def test_read_master_yaml_returns_mapping():
    # rely on repository layout: backend/config/rules_configurations/master.yaml
    data = FileManager.read_config_file("master.yaml")
    assert isinstance(data, dict)
    # master.yaml should reference other config files (like Upgrades, SoldierTypes, SquadRules)
    assert len(data) > 0
    # common key used by Config loader
    assert any(k for k in data.keys())

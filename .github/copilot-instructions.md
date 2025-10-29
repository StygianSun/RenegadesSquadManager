Purpose
-------
This file gives concise, actionable guidance for an AI coding agent to be productive in the RenegadesSquadManager repo.

High-level architecture (what to know fast)
-----------------------------------------
- Frontend: PySide6 Qt GUI lives in `frontend/`.
  - `frontend/main.py` constructs the QApplication and instantiates MainWindow with `DataManager()` and `FileManager()`.
  - UI code is split into generated UI (`frontend/generated_ui/`) and manual logic in `frontend/core_ui/`.
- Backend: pure-Python app logic lives in `backend/` with three useful subareas:
  - `backend/config/` — YAML rule/config files live under `backend/config/rules_configurations/` and are loaded by `backend.config.config.Config`.
  - `backend/data_managers/` — `DataManager` (app state + validation) and `FileManager` (read/write .squad YAMLs).
  - `backend/models/` — domain models like `Squad`, `Soldier`, `SoldierType`, `Upgrade`, etc.
- Packaging: there is a `RSM.spec` (PyInstaller) and `build/` output present. `FileManager.read_config_file` supports running under PyInstaller via `sys._MEIPASS`.

Key data flow and conventions (concrete examples)
------------------------------------------------
- Configs are YAML under `backend/config/rules_configurations/`. They are loaded with:
  - `backend.config.config.Config.load_config()` -> calls `backend.data_managers.file_manager.FileManager.read_config_file(file)` which resolves paths differently when frozen (see `sys._MEIPASS`).
  - Example: `Config` uses `target_class.from_dict(key, data_config[key])` to instantiate model objects (see `backend/models/upgrade.py` and `backend/models/soldier_type.py`).
- Model deserialisation pattern:
  - Most models implement `@classmethod from_dict(cls, name, rules_dict)` that accepts the YAML key and dict and returns an instance.
  - Use this pattern when adding new domain types so `Config` can dynamically instantiate them.
  - Example: `backend/models/upgrade.py::Upgrade.from_dict(name, rules_dict)`.
- Persistence/serialization:
  - `Squad.toDict()` returns a YAML-serialisable representation used by `FileManager.saveSquad`.
  - `DataManager.loadSquad(file_data)` expects the dict shape written by `FileManager.saveSquad` (keys: `player_name`, `squad` → `name`, `soldiers`, `masteries`, etc.).

UI patterns & wiring
-------------------
- The UI uses generated classes from Qt Designer under `frontend/generated_ui/` and manual dialogs under `frontend/core_ui/`.
  - Connect UI actions in `MainWindow.setupMenu()` (e.g. `actionLoad_Squad.triggered.connect(self.loadSquad)`).
  - When adding dialogs, follow existing pattern: dialog `exec()` -> on accepted, call `DataManager` methods and then `MainWindow.updateUI()`.

Build, run, and debug notes
-------------------------
- Run the app locally (developer flow):
  - Activate your environment and run `python frontend/main.py` (uses PySide6).
  - On Windows, Qt will open; use the menu to load/save `.squad` files.
- Packaging: PyInstaller is used; `RSM.spec` exists and `build/` contains a built output. During packaging, config files are expected to be bundled; `FileManager.read_config_file` handles `sys._MEIPASS`.
- No automated test suite is present in the repo root. When adding tests, prefer small unit tests for `backend/models/*` and `backend/data_managers/*` using pytest.

Project-specific conventions and gotchas
--------------------------------------
- Dynamic class instantiation: `backend/config/config.Config.load_configs` relies on YAML keys mapping to class names (e.g., `Upgrade`, `SoldierType`) that must exist in `backend.models` and implement `from_dict`.
- Paths: `FileManager.read_config_file` uses `Path(os.getcwd()) / "backend" / "config" / "rules_configurations" / file` when not frozen — run scripts from repository root to ensure relative paths resolve.
- YAML shapes are authoritative: update or extend YAML keys carefully (follow existing keys like `is_rare`, `rare_cost`, `has_options`) because `from_dict` methods access those keys directly.
- UI separation: put non-UI logic in `backend/` and keep `frontend/core_ui/*` focused on UI glue and dialogs.

When editing or extending
------------------------
- To add a new configuration-driven model: add class in `backend/models/` with `from_dict` and update YAML in `backend/config/rules_configurations/`; `Config` will pick it up automatically if you use the top-level `master.yaml` mapping.
- To add a new dialog/window: add UI in `designs/` with Qt Designer, generate UI into `frontend/generated_ui/`, and write the logic in `frontend/core_ui/` mirroring `soldier_dialog.py` or `mastery_dialog.py`.

Where to look for examples
-------------------------
- Config-driven model instantiation: `backend/config/config.py` and `backend/models/upgrade.py` and `soldier_type.py`.
- File I/O and PyInstaller path handling: `backend/data_managers/file_manager.py`.
- UI wiring and DataManager usage: `frontend/main.py` and `frontend/core_ui/soldier_dialog.py`.

Quick examples you can copy
--------------------------
- Minimal `.squad` file shape (what `FileManager.loadSquad()` / `DataManager.loadSquad()` expect):

```yaml
player_name: Alice
squad:
  name: "Renegade Strike Team"
  soldiers:
    - name: "Kade"
      type: "Grunt"
      upgrades: ["Grenade", "Armor"]
      equipment: ["Rifle"]
      is_leader: true
      leader_ability: "Inspire"
      is_psymancer: false
      psymancer_ability: null
      psychic_powers: []
  masteries: ["Tactics"]
  leader: "Kade"
  psymancer: null
  wildcard: "Tactics"
```

- Example `from_dict` pattern (follow this when adding models so `Config` can auto-load):

```python
@classmethod
def from_dict(cls, name: str, rules: dict):
    # read required keys directly (YAML shapes are authoritative)
    foo = rules["foo"]
    bar = rules.get("bar", 0)
    return cls(name, foo, bar)
```

Developer workflows (commands)
------------------------------
- Create a venv and install minimal deps (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install PySide6 PyYAML
```

- Run the app (from repository root):

```powershell
python frontend/main.py
```

- Regenerate generated UI after editing a Qt `.ui` (example using pyside6-uic):

```powershell
pyside6-uic designs/mainwindow.ui -o frontend/generated_ui/mainwindow.py
```

- Build with PyInstaller using the included spec (bundles data according to spec):

```powershell
pyinstaller RSM.spec
```

Important gotchas / troubleshooting
----------------------------------
- Run commands from the repository root. `FileManager.read_config_file` resolves config paths using `os.getcwd()` when not frozen — running from another cwd will cause missing-config errors.
- When packaging, ensure the YAML files under `backend/config/rules_configurations/` are included in the PyInstaller spec (the app uses `sys._MEIPASS` at runtime).
- YAML keys are treated as authoritative. `Config.load_configs` maps top-level keys in `master.yaml` to class names in `backend.models` and calls their `from_dict`. If the YAML shape changes, update the corresponding `from_dict`.

Testing and small safety additions
--------------------------------
- There is no test suite in-tree; add tiny pytest modules under `tests/` focusing on:
  - `backend/models/*`: test `from_dict`, `toDict`, and `__eq__` behavior.
  - `backend/data_managers/file_manager.py`: test `read_config_file` path resolution by mocking `sys.frozen` and `sys._MEIPASS`.
- Keep tests fast — prefer pure-Python unit tests that don't start the Qt event loop.

Quick references (files to open first)
------------------------------------
- `backend/config/config.py` — dynamic config loading and `from_dict` dispatch.
- `backend/data_managers/file_manager.py` — YAML I/O and PyInstaller path handling.
- `backend/data_managers/data_manager.py` — populating UI-friendly collections and squad load/validation.
- `backend/models/*.py` — model shapes and `from_dict`/serialization patterns (see `upgrade.py`, `soldier_type.py`, `squad.py`).
- `frontend/main.py` and `frontend/core_ui/*` — how dialogs interact with `DataManager` and update UI.

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from frontend.generated_ui.add_soldier import Ui_AddSoldier as AddSoldierDialog
from frontend.core_ui.leadership import LeadershipDialog
from frontend.core_ui.psymancer import PsymancerDialog
from backend.data_managers.data_manager import DataManager
from backend.models.soldier import Soldier

class SoldierDialog(QtWidgets.QDialog, AddSoldierDialog):
    def __init__(self, data_manager: DataManager = None):
        super().__init__()
        self.setupUi(self)
        self.data_manager = data_manager
        self.resize_upgrades()
        self.upgrades_tree.itemChanged.connect(self.handle_upgrade)
        self.is_leader_checkbox.stateChanged.connect(self.handle_leader)
        self.checkLeader()
        self.is_psymancer_checkbox.stateChanged.connect(self.handle_psymancer)
        self.checkPsymancer()
        self.load_types()
        self.loadEquipment()
        self.equipped_items_table.customContextMenuRequested.connect(self.showTableContext)
        self.add_equipment_button.clicked.connect(self.addEquipment)
        self.soldier = Soldier()
        self.equipped_items_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

    def editSoldier(self, soldier: Soldier = None):
        self.soldier = soldier
        self.soldier_name.setText(soldier.name)
        self.soldier_type_combo.blockSignals(True)
        self.soldier_type_combo.setCurrentText(soldier.type.name)
        self.soldier_type_combo.blockSignals(False)
        self.set_upgrades([upgrade for upgrade in soldier.type.upgrades])
        self.upgrades_tree.blockSignals(True)
        self.checkUpgrades(soldier.upgrades)
        self.upgrades_tree.blockSignals(False)
        self.equipped_items_table.blockSignals(True)
        self.checkEquipment(soldier.equipment)
        self.equipped_items_table.blockSignals(False)
        self.is_leader_checkbox.blockSignals(True)
        if soldier.is_leader:
            self.is_leader_checkbox.setCheckState(Qt.CheckState.Checked)
            self.is_leader_checkbox.setDisabled(False)
        self.is_leader_checkbox.blockSignals(False)
        self.is_psymancer_checkbox.blockSignals(True)
        if soldier.is_psymancer:
            self.is_psymancer_checkbox.setCheckState(Qt.CheckState.Checked)
            self.is_psymancer_checkbox.setDisabled(False)
        self.is_psymancer_checkbox.blockSignals(False)
        self.update_ui()

    def checkUpgrades(self, upgrades: list = None):
        for upgrade in upgrades:
            for i in range(self.upgrades_tree.topLevelItemCount()):
                item = self.upgrades_tree.topLevelItem(i)
                self._checkUpgradesHelper(item, upgrade)

    def _checkUpgradesHelper(self, treeItem, upgrade):
        if treeItem.text(0) == upgrade.name:
            treeItem.setCheckState(0, Qt.CheckState.Checked)
            if treeItem.childCount() > 0:
                for i in range(treeItem.childCount()):
                    child_item = treeItem.child(i)
                    child_item.setFlags(child_item.flags() | Qt.ItemIsEnabled)
        else:
            for i in range(treeItem.childCount()):
                child_item = treeItem.child(i)
                self._checkUpgradesHelper(child_item, upgrade)

    def checkEquipment(self, equipment: list = None):
        for equipment_object in equipment:
            rarity_text = ""
            if equipment_object.is_rare:
                for _ in range(equipment_object.rare_cost):
                    rarity_text += u'\u2605'
            range_text = ""
            if equipment_object.range == -1:
                range_text = "Long (" + u'\u221E' + ")"
            elif equipment_object.range == 18:
                range_text = "Medium (18\")"
            elif equipment_object.range == 9:
                range_text = "Short (9\")"
            elif equipment_object.range == 1:
                range_text = "Melee (1\")"
            elif equipment_object.range == 0:
                range_text = "-"
            else:
                range_text = str(equipment_object.range) + "\""
            atk_dice_text = str(equipment_object.attack_dice) if equipment_object.attack_dice != 0 else "-"
            dmg_text = str(equipment_object.dmg) if equipment_object.dmg != 0 else "-"
            row_pos = self.equipped_items_table.rowCount()
            self.equipped_items_table.insertRow(row_pos)
            for col, text in enumerate([equipment_object.name, str(equipment_object.cost), rarity_text, range_text, atk_dice_text, 
                                        dmg_text]):
                self.equipped_items_table.setItem(row_pos, col, QtWidgets.QTableWidgetItem(text))

    def resize_upgrades(self):
        self.upgrades_tree.expandAll()
        for i in range(self.upgrades_tree.columnCount()):
            self.upgrades_tree.resizeColumnToContents(i)

    def checkLeader(self):
        if self.data_manager.squad.hasLeader():
            self.is_leader_checkbox.setDisabled(True)

    def checkPsymancer(self):
        if self.data_manager.squad.hasPsymancer():
            self.is_psymancer_checkbox.setDisabled(True)

    def load_types(self):
        self.soldier_type_combo.addItem(" ")
        self.soldier_type_combo.addItems(list(self.data_manager.CONFIG.SOLDIER_TYPES.keys()))
        self.soldier_type_combo.currentTextChanged.connect(self.update_on_soldier_type)

    def update_on_soldier_type(self):
        cost = 0
        vitality = 0
        slots = 0
        ap = 0
        base_move = 0
        dash_move = "D0"
        move_type = ["Normal"]
        soldier_type = self.soldier_type_combo.currentText()
        abilities = []
        soldier_object = None
        rares_allowed = True
        if soldier_type != " ":
            soldier_object = self.data_manager.CONFIG.SOLDIER_TYPES[soldier_type]
            cost = soldier_object.cost
            vitality = soldier_object.vitality
            slots = soldier_object.max_slots
            ap = soldier_object.ap
            base_move = soldier_object.base_move
            dash_move = soldier_object.dash_move
            move_type = soldier_object.move_type
            rares_allowed = soldier_object.rares_allowed
        self.soldier.type = soldier_object
        self.soldier.vitality = vitality
        self.soldier.max_slots = slots
        self.soldier.ap = ap
        self.soldier.base_move = base_move
        self.soldier.dash_move = dash_move
        self.soldier.move_type = move_type
        self.soldier.cost = cost
        self.soldier.rares_allowed = rares_allowed
        if soldier_type != " ":
            for ability in soldier_object.abilities:
                ability_object = self.data_manager.CONFIG.ABILITIES[ability]
                abilities.append(ability_object)
        self.soldier.abilities = abilities
        self.set_upgrades(soldier_object.upgrades)
        self.update_ui()

    def disableRares(self):
        for i in range(self.equipment_combo.count()):
            item = self.equipment_combo.model().item(i)
            equipment = self.data_manager.CONFIG.EQUIPMENT[item.text()] if item.text() != " " else None
            if equipment is not None and equipment.is_rare:
                item.setEnabled(False)

    def enableRares(self):
        for i in range(self.equipment_combo.count()):
            item = self.equipment_combo.model().item(i)
            item.setEnabled(True)

    def disableEquipment(self):
        self.equipment_combo.setEnabled(False)
        self.equipment_type_combo.setEnabled(False)

    def enableEquipment(self):
        self.equipment_combo.setEnabled(True)
        self.equipment_type_combo.setEnabled(True)

    def disableItems(self):
        for i in range(self.equipment_type_combo.count()):
            item = self.equipment_type_combo.model().item(i)
            if item.text() == "Items":
                item.setEnabled(False)
    
    def enableItems(self):
        for i in range(self.equipment_type_combo.count()):
            item = self.equipment_type_combo.model().item(i)
            if item.text() == "Items":
                item.setEnabled(True)

    def disableMelee(self):
        for i in range(self.equipment_type_combo.count()):
            item = self.equipment_type_combo.model().item(i)
            if item.text() == "Melee Weapons":
                item.setEnabled(False)
    
    def enableMelee(self):
        for i in range(self.equipment_type_combo.count()):
            item = self.equipment_type_combo.model().item(i)
            if item.text() == "Melee Weapons":
                item.setEnabled(True)

    def loadEquipment(self):
        self.equipment_type_combo.addItems([" ", "Ranged Weapons", "Melee Weapons", "Items"])
        self.equipment_type_combo.currentTextChanged.connect(self.updateOnEquipmentType)

    def updateOnEquipmentType(self):
        self.equipment_combo.clear()
        self.equipment_combo.addItem(" ")
        match self.equipment_type_combo.currentText():
            case "Ranged Weapons":
                self.equipment_combo.addItems(self.data_manager.RANGED_WEAPONS.keys())
            case "Melee Weapons":
                self.equipment_combo.addItems(self.data_manager.MELEE_WEAPONS.keys())
            case "Items":
                self.equipment_combo.addItems(self.data_manager.ITEMS)
        self.checkAllowedEquipment()

    def checkAllowedEquipment(self):
        if self.soldier_type_combo.currentText() != " ":
            if not self.soldier.rares_allowed:
                self.disableRares()
            else:
                self.enableRares()
            if not self.soldier.type.items_allowed:
                self.disableItems()
            else:
                self.enableItems()
            if not self.soldier.type.equipment_allowed:
                self.disableEquipment()
            else:
                self.enableEquipment()
            if not self.soldier.type.melee_allowed:
                self.disableMelee()
            else:
                self.enableMelee()
        
    def update_ui(self):
        self.soldier.validate(self.data_manager)
        cost_text = str(self.soldier.cost)
        vitality_text = str(self.soldier.vitality)
        slots_text = str(self.soldier.cur_slots) + "/" + str(self.soldier.max_slots)
        ap_text = str(self.soldier.ap)
        move_text = (str(self.soldier.base_move) + "\" + " + self.soldier.dash_move + " " +
                        ", ".join(self.soldier.move_type))
        rarity_text = ""
        abilities_text = ""
        leader_bonus_text = self.soldier.leader_ability.name if self.soldier.leader_ability is not None else ""
        psymancer_type_text = self.soldier.psymancer_ability.name if self.soldier.psymancer_ability is not None else ""
        psychic_powers_text = ", ".join([power.name for power in self.soldier.psychic_powers])
        upgrades = []
        if self.soldier.type is not None:
            if self.soldier.type.is_rare:
                for _ in range(self.soldier.type.rare_cost):
                    rarity_text += u'\u2605'
            upgrades = self.soldier.type.upgrades
            abilities_text = ", ".join(ability.name for ability in self.soldier.abilities)
        self.checkAllowedEquipment()
        self.cost_text.setText(cost_text)
        self.vitality_text.setText(vitality_text)
        self.slots_text.setText(slots_text)
        self.ap_text.setText(ap_text)
        self.move_text.setText(move_text)
        self.abilities_text.setText(abilities_text)
        self.rarity_text.setText(rarity_text)
        self.leader_bonus_text.setText(leader_bonus_text)
        self.psymancer_type_text.setText(psymancer_type_text)
        self.psychic_powers_text.setText(psychic_powers_text)

    def set_upgrades(self, upgrades: list[str] = None):
        if upgrades is None:
            self.upgrades_tree.clear()
        else:
            self.upgrades_tree.clear()
            upgrade_items = []
            for upgrade in upgrades:
                upgrade_object = self.data_manager.CONFIG.UPGRADES[upgrade]
                rarity = ""
                if upgrade_object.is_rare:
                    for _ in range(upgrade_object.rare_cost):
                        rarity += u'\u2605'
                upgrade_item = QtWidgets.QTreeWidgetItem([upgrade,
                                                          str(upgrade_object.cost), str(rarity)])
                upgrade_item.setFlags(upgrade_item.flags() | Qt.ItemIsUserCheckable)
                upgrade_item.setCheckState(0, Qt.Unchecked)
                if len(upgrade_object.has_options) > 0:
                    for option in upgrade_object.has_options:
                        option_object = self.data_manager.CONFIG.UPGRADES[option]
                        rarity = ""
                        if option_object.is_rare:
                            for _ in range(option_object.rare_cost):
                                rarity += u'\u2605'
                        option_item = QtWidgets.QTreeWidgetItem([option,
                                                                 str(option_object.cost), str(rarity)])
                        option_item.setFlags(option_item.flags() | Qt.ItemIsUserCheckable)
                        option_item.setFlags(option_item.flags() & ~Qt.ItemIsEnabled)
                        option_item.setCheckState(0, Qt.Unchecked)
                        upgrade_item.addChild(option_item)
                    upgrade_item.setExpanded(True)
                upgrade_items.append(upgrade_item)
            self.upgrades_tree.insertTopLevelItems(0, upgrade_items)
        self.resize_upgrades()

    def handle_upgrade(self, item, column):
        state = item.checkState(column)
        text = item.text(column)
        if state == Qt.CheckState.Checked:
            self.upgrades_tree.blockSignals(True)
            for i in range(item.childCount()):
                child = item.child(i)
                child.setFlags(child.flags() | Qt.ItemIsEnabled)
            self.upgrades_tree.blockSignals(False)
            self.apply_upgrade(text)
        elif state == Qt.CheckState.Unchecked:
            self.upgrades_tree.blockSignals(True)
            for i in range(item.childCount()):
                child = item.child(i)
                child.setFlags(child.flags() & ~Qt.ItemIsEnabled)
                if child.checkState(0) == Qt.CheckState.Checked:
                    child.setCheckState(0, Qt.Unchecked)
                    self.unapply_upgrade(child.text(column))
            self.upgrades_tree.blockSignals(False)
            self.unapply_upgrade(text)
        self.update_ui()
    
    def apply_upgrade(self, upgrade):
        upgrade_object = self.data_manager.CONFIG.UPGRADES[upgrade]
        self.soldier.upgrades.append(upgrade_object)
        self.soldier.cost += upgrade_object.cost
        self.soldier.abilities.extend(self.data_manager.CONFIG.ABILITIES[ability] for ability in upgrade_object.abilities)
        for modification in upgrade_object.modifications:
            if modification in ["weapon_type", "equipment", "weapon"]:
                pass #Handle non-standard mods
            else:
                if upgrade_object.modifications[modification]["mod"] == "add":
                    setattr(self.soldier, modification, getattr(self.soldier, modification) + 
                            upgrade_object.modifications[modification]["value"])
                elif upgrade_object.modifications[modification]["mod"] == "equals":
                    setattr(self.soldier, modification, upgrade_object.modifications[modification]["value"])

    def unapply_upgrade(self, upgrade):
        upgrade_object = self.data_manager.CONFIG.UPGRADES[upgrade]
        self.soldier.upgrades.remove(upgrade_object)
        self.soldier.cost -= upgrade_object.cost
        for ability in upgrade_object.abilities:
            print(ability)
            print(self.soldier.abilities)
            print(self.data_manager.CONFIG.ABILITIES[ability])
            self.soldier.abilities.remove(self.data_manager.CONFIG.ABILITIES[ability])
        for modification in upgrade_object.modifications:
            if modification in ["weapon_type", "equipment", "weapon"]:
                pass #Handle non-standard mods
            else:
                if upgrade_object.modifications[modification]["mod"] == "add":
                    if type(upgrade_object.modifications[modification]["value"]) is list:
                        new_upgrade_list = [item for item in getattr(self.soldier, modification) if 
                                            item not in upgrade_object.modifications[modification]["value"]]
                        setattr(self.soldier, modification, new_upgrade_list)
                    else:
                        setattr(self.soldier, modification, getattr(self.soldier, modification) -
                                upgrade_object.modifications[modification]["value"])
                elif upgrade_object.modifications[modification]["mod"] == "equals":
                    setattr(self.soldier, modification, getattr(self.soldier.type, modification))

    def handle_leader(self, state):
        if state == 2:
            if self.soldier_type_combo.currentText() != " ":
                dialog = LeadershipDialog(self.data_manager)
                dialog.accepted.connect(lambda: self.leader_selected(dialog.getAbility()))
                dialog.rejected.connect(lambda: self.leaderCanceled())
                dialog.exec()
            else:
                self.is_leader_checkbox.blockSignals(True)
                self.is_leader_checkbox.setCheckState(Qt.CheckState.Unchecked)
                self.is_leader_checkbox.blockSignals(False)
                #Error dialog
        elif state == 0:
            self.leader_unselected()
        self.update_ui()

    def leaderCanceled(self):
        self.is_leader_checkbox.blockSignals(True)
        self.is_leader_checkbox.setCheckState(Qt.CheckState.Unchecked)
        self.is_leader_checkbox.blockSignals(False)

    def leader_selected(self, ability: str = ''):
        if self.soldier_type_combo.currentText() != " ":
            self.soldier.leader_ability = self.data_manager.CONFIG.UPGRADES[ability]
            for ability in self.soldier.leader_ability.abilities:
                self.soldier.abilities.append(self.data_manager.CONFIG.ABILITIES[ability])
            self.soldier.is_leader = True
            self.soldier.cost += (self.soldier.vitality * self.soldier.leader_ability.cost)
        else:
            self.is_leader_checkbox.blockSignals(True)
            self.is_leader_checkbox.setCheckState(Qt.CheckState.Unchecked)
            self.is_leader_checkbox.blockSignals(False)
   
    def leader_unselected(self):
        self.soldier.is_leader = False
        self.soldier.cost -= (self.soldier.vitality * self.soldier.leader_ability.cost)
        for ability in self.soldier.leader_ability.abilities:
            self.soldier.abilities.remove(self.data_manager.CONFIG.ABILITIES[ability])
        self.soldier.leader_ability = None

    def handle_psymancer(self, state):
        if state == 2:
            if self.soldier_type_combo.currentText() != " ":
                dialog = PsymancerDialog(self.data_manager)
                dialog.accepted.connect(lambda: self.psymancerSelected(dialog.getData()))
                dialog.rejected.connect(lambda: self.psymancerCanceled())
                dialog.exec()
            else:
                self.is_psymancer_checkbox.blockSignals(True)
                self.is_psymancer_checkbox.setCheckState(Qt.CheckState.Unchecked)
                self.is_psymancer_checkbox.blockSignals(False)
                #Error dialog
        elif state == 0:
            self.psymancerUnselected()
        self.update_ui()

    def psymancerCanceled(self):
        self.is_psymancer_checkbox.blockSignals(True)
        self.is_psymancer_checkbox.setCheckState(Qt.CheckState.Unchecked)
        self.is_psymancer_checkbox.blockSignals(False)

    def psymancerSelected(self, powers: list[str] = []):
        if self.soldier_type_combo.currentText() != " ":
            self.soldier.psymancer_ability = self.data_manager.CONFIG.UPGRADES[powers[0]]
            for ability in self.soldier.psymancer_ability.abilities:
                self.soldier.abilities.append(self.data_manager.CONFIG.ABILITIES[ability])
            for power in powers[1:]:
                if power != " ":
                    self.soldier.psychic_powers.append(self.data_manager.CONFIG.UPGRADES[power])
            for power in self.soldier.psychic_powers:
                for ability in power.abilities:
                    self.soldier.abilities.append(self.data_manager.CONFIG.ABILITIES[ability])
            self.soldier.is_psymancer = True
            self.soldier.cost += (self.soldier.vitality * self.soldier.psymancer_ability.cost)
        else:
            self.is_psymancer_checkbox.blockSignals(True)
            self.is_psymancer_checkbox.setCheckState(Qt.CheckState.Unchecked)
            self.is_psymancer_checkbox.blockSignals(False)

    def psymancerUnselected(self):
        self.soldier.is_psymancer = False
        self.soldier.cost -= (self.soldier.vitality * self.soldier.psymancer_ability.cost)
        for power in self.soldier.psychic_powers:
            for ability in power.abilities:
                self.soldier.abilities.remove(self.data_manager.CONFIG.ABILITIES[ability])
        self.soldier.psychic_powers = []
        for ability in self.soldier.psymancer_ability.abilities:
            self.soldier.abilities.remove(self.data_manager.CONFIG.ABILITIES[ability])
        self.soldier.psymancer_ability = None

    def addEquipment(self):
        equipment = self.equipment_combo.currentText()
        equipment_object = self.data_manager.CONFIG.EQUIPMENT[equipment]
        if self.soldier.cur_slots + equipment_object.slots > self.soldier.max_slots or equipment == " ":
            #oops, error
            pass
        else:
            self.soldier.equipment.append(equipment_object)
            self.soldier.cur_slots += equipment_object.slots
            if type(equipment_object.cost) is str:
                self.soldier.cost += (self.soldier.vitality * int(equipment_object.cost[0]))
            else:
                self.soldier.cost += equipment_object.cost
            rarity_text = ""
            if equipment_object.is_rare:
                for _ in range(equipment_object.rare_cost):
                    rarity_text += u'\u2605'
            range_text = ""
            if equipment_object.range == -1:
                range_text = "Long (" + u'\u221E' + ")"
            elif equipment_object.range == 18:
                range_text = "Medium (18\")"
            elif equipment_object.range == 9:
                range_text = "Short (9\")"
            elif equipment_object.range == 1:
                range_text = "Melee (1\")"
            elif equipment_object.range == 0:
                range_text = "-"
            else:
                range_text = str(equipment_object.range) + "\""
            atk_dice_text = str(equipment_object.attack_dice) if equipment_object.attack_dice != 0 else "-"
            dmg_text = str(equipment_object.dmg) if equipment_object.dmg != 0 else "-"
            row_pos = self.equipped_items_table.rowCount()
            self.equipped_items_table.insertRow(row_pos)
            for col, text in enumerate([equipment, str(equipment_object.cost), rarity_text, range_text, atk_dice_text, 
                                        dmg_text]):
                self.equipped_items_table.setItem(row_pos, col, QtWidgets.QTableWidgetItem(text))
        self.update_ui()

    def showTableContext(self, pos):
        global_pos = self.equipped_items_table.viewport().mapToGlobal(pos)
        item = self.equipped_items_table.itemAt(pos)
        if item:
            menu = QtWidgets.QMenu(self)
            delete_action = menu.addAction("Delete Equipment")
            action = menu.exec(global_pos)

            if action == delete_action:
                index = item.row()
                if index >= 0 and index < self.equipped_items_table.rowCount():
                    item_to_remove = self.equipped_items_table.item(index, 0).text()
                    self.equipped_items_table.removeRow(index)
                    self.soldier.equipment.remove(self.data_manager.CONFIG.EQUIPMENT[item_to_remove])
        self.update_ui()
    
    def getSoldier(self):
        self.soldier.name = self.soldier_name.toPlainText()
        return self.soldier
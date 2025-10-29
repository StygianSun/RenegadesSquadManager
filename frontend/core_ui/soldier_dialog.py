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
        self.soldier_type_combo.setCurrentText(soldier.soldier_type.name)
        self.soldier_type_combo.blockSignals(False)
        self.set_upgrades([upgrade for upgrade in soldier.soldier_type.upgrades])
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
            equipment_text = equipment_object.toFormattedDict()
            row_pos = self.equipped_items_table.rowCount()
            self.equipped_items_table.insertRow(row_pos)
            for col, text in enumerate([equipment_text["name"], equipment_text["cost"], equipment_text["rarity"],
                                        equipment_text["range"], equipment_text["atk_dice"], equipment_text["dmg"]]):
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
        soldier_type = self.soldier_type_combo.currentText()
        if soldier_type != " ":
            soldier_object = self.data_manager.CONFIG.SOLDIER_TYPES[soldier_type]
        else:
            soldier_object = self.data_manager.getDefaultSoldierType()
        self.data_manager.applyTypeToSoldier(self.soldier, soldier_object)
        self.set_upgrades(soldier_object.upgrades)
        self.update_ui()

    def disableRares(self):
        equipment_is_rare = self.data_manager.getIsEquipmentRare()
        for i in range(self.equipment_combo.count()):
            item = self.equipment_combo.model().item(i)
            if item.text() != " " and equipment_is_rare[item.text()]:
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
            allowed_equipment = self.data_manager.getAllowedEquipmentForSoldierType(self.soldier.soldier_type)
            if not allowed_equipment["rares"]:
                self.disableRares()
            else:
                self.enableRares()
            if not allowed_equipment["items"]:
                self.disableItems()
            else:
                self.enableItems()
            if not allowed_equipment["equipment"]:
                self.disableEquipment()
            else:
                self.enableEquipment()
            if not allowed_equipment["melee"]:
                self.disableMelee()
            else:
                self.enableMelee()
        
    def update_ui(self):
        self.soldier.validate(self.data_manager)
        display_texts = self.soldier.getDisplayTexts()
        self.checkAllowedEquipment()
        self.cost_text.setText(display_texts["cost"])
        self.vitality_text.setText(display_texts["vitality"])
        self.slots_text.setText(display_texts["slots"])
        self.ap_text.setText(display_texts["ap"])
        self.move_text.setText(display_texts["move"])
        self.abilities_text.setText(display_texts["abilities"])
        self.rarity_text.setText(display_texts["rarity"])
        self.leader_bonus_text.setText(display_texts["leader_ability"])
        self.psymancer_type_text.setText(display_texts["psymancer_ability"])
        self.psychic_powers_text.setText(display_texts["psychic_powers"])

    def set_upgrades(self, upgrades: list[str] = None):
        if upgrades is None:
            self.upgrades_tree.clear()
        else:
            self.upgrades_tree.clear()
            upgrade_items = []
            for upgrade in upgrades:
                formatted_upgrade = self.data_manager.getFormattedUpgrade(upgrade)
                upgrade_item = QtWidgets.QTreeWidgetItem([upgrade,
                                                          str(formatted_upgrade["cost"]), str(formatted_upgrade["rarity"])])
                upgrade_item.setFlags(upgrade_item.flags() | Qt.ItemIsUserCheckable)
                upgrade_item.setCheckState(0, Qt.Unchecked)
                if len(formatted_upgrade["has_options"]) > 0:
                    for option in formatted_upgrade["has_options"]:
                        formatted_option = self.data_manager.getFormattedUpgrade(option)
                        option_item = QtWidgets.QTreeWidgetItem([option,
                                                                 str(formatted_option["cost"]), str(formatted_option["rarity"])])
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
            self.data_manager.applySoldierUpgrade(self.soldier, text)
        elif state == Qt.CheckState.Unchecked:
            self.upgrades_tree.blockSignals(True)
            for i in range(item.childCount()):
                child = item.child(i)
                child.setFlags(child.flags() & ~Qt.ItemIsEnabled)
                if child.checkState(0) == Qt.CheckState.Checked:
                    child.setCheckState(0, Qt.Unchecked)
                    self.data_manager.unapplySoldierUpgrade(self.soldier, child.text(column))
            self.upgrades_tree.blockSignals(False)
            self.data_manager.unapplySoldierUpgrade(self.soldier, text)
        self.update_ui()

    def handle_leader(self, state):
        if state == 2:
            if self.soldier_type_combo.currentText() != " ":
                dialog = LeadershipDialog(self.data_manager)
                dialog.accepted.connect(lambda: self.leader_selected(dialog.getAbility()))
                dialog.rejected.connect(lambda: self.leaderCanceled())
                dialog.exec()
            else:
                self.leaderCanceled()
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
            self.data_manager.setSoldierAsLeader(self.soldier, ability)
        else:
            self.leaderCanceled()
   
    def leader_unselected(self):
        self.data_manager.unsetSoldierAsLeader(self.soldier)

    def handle_psymancer(self, state):
        if state == 2:
            if self.soldier_type_combo.currentText() != " ":
                dialog = PsymancerDialog(self.data_manager)
                dialog.accepted.connect(lambda: self.psymancerSelected(dialog.getData()))
                dialog.rejected.connect(lambda: self.psymancerCanceled())
                dialog.exec()
            else:
                self.psymancerCanceled()
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
            self.data_manager.setSoldierAsPsymancer(self.soldier, powers)
        else:
            self.psymancerCanceled()

    def psymancerUnselected(self):
        self.data_manager.unsetSoldierAsPsymancer(self.soldier)

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
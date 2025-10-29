import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QTimer

from frontend.generated_ui.mainwindow import Ui_MainWindow
from frontend.core_ui.soldier_dialog import SoldierDialog
from frontend.core_ui.mastery_dialog import MasteryDialog
from backend.data_managers.data_manager import DataManager
from backend.data_managers.file_manager import FileManager


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, data_manager: DataManager = None, file_manager: FileManager = None):
        super().__init__()
        self.setupUi(self)
        self.data_manager = data_manager
        self.file_manager = file_manager
        self.add_soldier_button.clicked.connect(self.add_soldier)
        self.add_mastery_button.clicked.connect(self.add_mastery)
        self.squad_members_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.squad_mastery_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.rares_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.squad_members_table.customContextMenuRequested.connect(self.showSoldierContext)
        self.squad_mastery_table.customContextMenuRequested.connect(self.showMasteryContext)
        self.setupMenu()
        self.updateUI()

    def add_soldier(self):
        dialog = SoldierDialog(self.data_manager)
        dialog.accepted.connect(lambda: self.soldier_added(dialog.getSoldier()))
        dialog.exec()

    def soldier_added(self, soldier):
        self.data_manager.addSoldierToSquad(soldier)
        self.data_manager.validateSquad()
        self.updateUI()

    def add_mastery(self):
        dialog = MasteryDialog(self.data_manager)
        dialog.accepted.connect(lambda: self.masteryAdded(dialog.getMastery()))
        dialog.exec()

    def masteryAdded(self, mastery):
        self.data_manager.addMasteryToSquad(mastery)
        self.data_manager.validateSquad()
        self.updateUI()

    def setupMenu(self):
        self.actionNew_Squad.triggered.connect(self.newSquad)
        self.actionSave_Squad.triggered.connect(self.saveSquad)
        self.actionSave_Squad_As.triggered.connect(self.saveSquadAs)
        self.actionLoad_Squad.triggered.connect(self.loadSquad)
        self.actionGenerate_PDF.triggered.connect(self.generatePDF)

    def newSquad(self):
        if self.file_manager.loaded_file is None:
            if not self.data_manager.squad.isEmpty():
                if self.unsavedFile():
                    self.data_manager.newSquad()
                    self.updateUI()
        else:
            if self.data_manager.squadChanged():
                if self.unsavedFile():
                    self.data_manager.newSquad()
                    self.updateUI()
            else:
                self.data_manager.newSquad()
                self.updateUI()
            

    def unsavedFile(self):
        window = QtWidgets.QMessageBox(self)
        window.setWindowTitle("Squad Not Saved")
        window.setText("This squad is unsaved, do you wish to save it now?")
        window.setIcon(QtWidgets.QMessageBox.Warning)

        accept_button = QtWidgets.QPushButton("Save Now")
        cancel_button = QtWidgets.QPushButton("Cancel")

        window.addButton(accept_button, QtWidgets.QMessageBox.AcceptRole)
        window.addButton(cancel_button, QtWidgets.QMessageBox.RejectRole)

        accept_button.clicked.connect(self.saveSquadAs)

        result = window.exec()
        if result == 2:
            return True
        else:
            return False

    def saveSquad(self):
        if self.file_manager.loaded_file is None:
            self.saveSquadAs()
        else:
            self.file_manager.saveSquad(self.data_manager.squad)

    def saveSquadAs(self):
        self.file_manager.loaded_file, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Squad Files (*.squad);;All Files(*)"
        )
        if self.file_manager.loaded_file:
            self.data_manager.squad.player_name = self.player_name.text()
            self.data_manager.squad.name = self.squad_name.text()
            self.file_manager.saveSquad(self.data_manager.squad)

    def loadSquad(self):
        self.file_manager.loaded_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open Squad File",
            "",
            "Squad Files (*.squad);;All Files(*)"
        )
        if self.file_manager.loaded_file:
            self.data_manager.loadSquad(self.file_manager.loadSquad())
        self.player_name.setText(self.data_manager.squad.player_name)
        self.squad_name.setText(self.data_manager.squad.name)
        self.updateUI()

    def generatePDF(self):
        pass

    def updateUI(self):
        squad_cost = 0
        rares_list = []
        self.squad_members_table.setRowCount(0)
        self.squad_mastery_table.setRowCount(0)
        self.rares_table.setRowCount(0)
        for soldier in self.data_manager.squad.soldiers:
            squad_cost += soldier.cost
            soldier_name = soldier.name
            soldier_type = soldier.type.name
            soldier_cost = str(soldier.cost)
            soldier_upgrades = []
            for upgrade in soldier.upgrades:
                soldier_upgrades.append(upgrade.name)
                if upgrade.is_rare:
                    rares_list.append(upgrade)
            soldier_equipment = []
            for equipment in soldier.equipment:
                soldier_equipment.append(equipment.name)
                if equipment.is_rare:
                    rares_list.append(equipment)
            soldier_leader = "Yes" if soldier.is_leader else ""
            soldier_psy_grade = soldier.psymancer_ability.name if soldier.psymancer_ability is not None else ""
            soldier_psymancer = "Yes, " + soldier_psy_grade if soldier.is_psymancer else ""
            row_pos = self.squad_members_table.rowCount()
            self.squad_members_table.insertRow(row_pos)
            for col, text in enumerate(
                                [soldier_name, soldier_type, soldier_leader, soldier_psymancer, soldier_cost,
                                 ", ".join(soldier_upgrades), ", ".join(soldier_equipment)]
                            ):
                self.squad_members_table.setItem(row_pos, col, QtWidgets.QTableWidgetItem(text))
            if soldier.type.is_rare:
                rares_list.append(soldier.type)
        for rare in rares_list:
            row_pos = self.rares_table.rowCount()
            self.rares_table.insertRow(row_pos)
            rare_name = rare.name
            rarity = ""
            for _ in range(rare.rare_cost):
                rarity += u'\u2605'
            for col, text in enumerate([rare_name, rarity]):
                self.rares_table.setItem(row_pos, col, QtWidgets.QTableWidgetItem(text))
        self.total_cost_text.setText(str(squad_cost))
        for mastery in self.data_manager.squad.masteries:
            mastery_name = mastery.name
            mastery_powers = ", ".join(mastery.powers)
            mastery_type = mastery.type
            row_pos = self.squad_mastery_table.rowCount()
            self.squad_mastery_table.insertRow(row_pos)
            for col, text in enumerate([mastery_name, mastery_type, mastery_powers]):
                self.squad_mastery_table.setItem(row_pos, col, QtWidgets.QTableWidgetItem(text))
        self.resize(self.sizeHint())

    def showSoldierContext(self, pos):
        global_pos = self.squad_members_table.viewport().mapToGlobal(pos)
        item = self.squad_members_table.itemAt(pos)
        if item:
            menu = QtWidgets.QMenu(self)
            edit_action = menu.addAction("Edit Soldier")
            duplicate_action = menu.addAction("Duplicate Soldier")
            delete_action = menu.addAction("Remove Soldier")
            action = menu.exec(global_pos)

            index = item.row()
            if index >= 0 and index < self.squad_members_table.rowCount():
                if action == delete_action:
                    self.squad_members_table.removeRow(index)
                    self.data_manager.removeSoldier(index)
                    self.data_manager.validateSquad()
                elif action == edit_action:
                    dialog = SoldierDialog(self.data_manager)
                    dialog.editSoldier(self.data_manager.getSoldier(index))
                    dialog.accepted.connect(lambda: self.data_manager.editSoldier(index, dialog.getSoldier()))
                    dialog.exec()
                    self.data_manager.validateSquad()
                elif action == duplicate_action:
                    self.data_manager.duplicateSoldier(index)
                    self.data_manager.validateSquad()
        self.updateUI()

    def showMasteryContext(self, pos):
        global_pos = self.squad_mastery_table.viewport().mapToGlobal(pos)
        item = self.squad_mastery_table.itemAt(pos)
        if item:
            menu = QtWidgets.QMenu(self)
            delete_action = menu.addAction("Remove Mastery")
            action = menu.exec(global_pos)

            if action == delete_action:
                index = item.row()
                if index >= 0 and index < self.squad_mastery_table.rowCount():
                    item_to_remove = self.squad_mastery_table.item(index, 0).text()
                    self.squad_mastery_table.removeRow(index)
                    self.data_manager.squad.masteries.remove(self.data_manager.CONFIG.MASTERIES[item_to_remove])
        self.updateUI()

        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow(DataManager(), FileManager())
window.show()
app.exec()
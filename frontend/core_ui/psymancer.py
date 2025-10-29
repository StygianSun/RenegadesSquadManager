from PySide6 import QtWidgets
from frontend.generated_ui.psymancer import Ui_Psymancer as AddPsymancerDialog
from backend.data_managers.data_manager import DataManager
from PySide6.QtCore import Qt

class PsymancerDialog(QtWidgets.QDialog, AddPsymancerDialog):
    def __init__(self, data_manager: DataManager = None):
        super().__init__()
        self.setupUi(self)
        self.data_manager = data_manager
        self.setupComboBoxes()

    def getData(self):
        psymancer_grade = self.grade_combo_box.currentText()
        power_1 = self.power_1_combo.currentText()
        power_2 = self.power_2_combo.currentText()
        power_3 = self.power_3_combo.currentText()
        return [psymancer_grade, power_1, power_2, power_3]
    
    def setupComboBoxes(self):
        self.grade_combo_box.addItem(" ")
        self.grade_combo_box.addItems(self.data_manager.PSYMANCER_ABILITIES.keys())
        self.grade_combo_box.currentTextChanged.connect(self.enablePowerCombos)
        self.power_1_combo.addItem(" ")
        self.power_1_combo.addItems(self.data_manager.PSYCHIC_POWERS.keys())
        self.power_1_combo.currentTextChanged.connect(self.disableSelectedItems)
        self.power_2_combo.addItem(" ")
        self.power_2_combo.addItems(self.data_manager.PSYCHIC_POWERS.keys())
        self.power_2_combo.currentTextChanged.connect(self.disableSelectedItems)
        self.power_3_combo.addItem(" ")
        self.power_3_combo.addItems(self.data_manager.PSYCHIC_POWERS.keys())
        self.power_3_combo.currentTextChanged.connect(self.disableSelectedItems)

    def enablePowerCombos(self):
        if self.grade_combo_box.currentText() != " ":
            self.power_1_combo.setEnabled(True)
            self.power_2_combo.setEnabled(True)
            if self.data_manager.getPsymancerPowerCount(self.grade_combo_box.currentText()) == 3:
                self.power_3_combo.setEnabled(True)
        else:
            self.power_1_combo.setEnabled(False)
            self.power_2_combo.setEnabled(False)
            self.power_3_combo.setEnabled(False)

    def disableSelectedItems(self):
        self.power_1_combo.blockSignals(True)
        self.power_2_combo.blockSignals(True)
        self.power_3_combo.blockSignals(True)
        power_1 = self.power_1_combo.currentText()
        power_2 = self.power_2_combo.currentText()
        power_3 = self.power_3_combo.currentText()
        for i in range(self.power_1_combo.count()):
            item = self.power_1_combo.model().item(i)
            if item.text() != " " and (item.text() == power_2 or item.text() == power_3):
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        for i in range(self.power_2_combo.count()):
            item = self.power_2_combo.model().item(i)
            if item.text() != " " and (item.text() == power_1 or item.text() == power_3):
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        for i in range(self.power_3_combo.count()):
            item = self.power_3_combo.model().item(i)
            if item.text() != " " and (item.text() == power_1 or item.text() == power_2):
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        self.power_1_combo.blockSignals(False)
        self.power_2_combo.blockSignals(False)
        self.power_3_combo.blockSignals(False)
                

    def power1Changed(self):
        power_1 = self.power_1_combo.currentText()
        if power_1 != " ":
            self.power_2_combo.blockSignals(True)
            self.power_3_combo.blockSignals(True)
            if power_1 == self.power_2_combo.currentText():
                self.power_2_combo.setCurrentIndex(0)
            if power_1 == self.power_3_combo.currentText():
                self.power_3_combo.setCurrentIndex(0)
        for i in range(self.power_2_combo.count()):
            item = self.power_2_combo.model().item(i)
            if self.power_2_combo.itemText(i) == power_1 and power_1 != " ":
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        for i in range(self.power_3_combo.count()):
            item = self.power_3_combo.model().item(i)
            if self.power_3_combo.itemText(i) == power_1 and power_1 != " ":
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        self.power_2_combo.blockSignals(False)
        self.power_3_combo.blockSignals(False)
    
    def power2Changed(self):
        power_2 = self.power_2_combo.currentText()
        if power_2 != " ":
            self.power_1_combo.blockSignals(True)
            self.power_3_combo.blockSignals(True)
            if power_2 == self.power_1_combo.currentText():
                self.power_1_combo.setCurrentIndex(0)
            if power_2 == self.power_3_combo.currentText():
                self.power_3_combo.setCurrentIndex(0)
        for i in range(self.power_1_combo.count()):
            item = self.power_1_combo.model().item(i)
            if self.power_1_combo.itemText(i) == power_2 and power_2 != " ":
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        for i in range(self.power_3_combo.count()):
            item = self.power_3_combo.model().item(i)
            if self.power_3_combo.itemText(i) == power_2 and power_2 != " ":
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        self.power_1_combo.blockSignals(False)
        self.power_3_combo.blockSignals(False)
    
    def power3Changed(self):
        power_3 = self.power_3_combo.currentText()
        if power_3 != " ":
            self.power_2_combo.blockSignals(True)
            self.power_1_combo.blockSignals(True)
            if power_3 == self.power_2_combo.currentText():
                self.power_2_combo.setCurrentIndex(0)
            if power_3 == self.power_1_combo.currentText():
                self.power_1_combo.setCurrentIndex(0)
        for i in range(self.power_2_combo.count()):
            item = self.power_2_combo.model().item(i)
            if self.power_2_combo.itemText(i) == power_3 and power_3 != " ":
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        for i in range(self.power_1_combo.count()):
            item = self.power_1_combo.model().item(i)
            if self.power_1_combo.itemText(i) == power_3 and power_3 != " ":
                item.setEnabled(False)
            else:
                item.setEnabled(True)
        self.power_2_combo.blockSignals(False)
        self.power_1_combo.blockSignals(False)
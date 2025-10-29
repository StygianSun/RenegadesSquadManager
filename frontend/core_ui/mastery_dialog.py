from PySide6 import QtWidgets
from frontend.generated_ui.add_mastery import Ui_AddMastery as AddMasteryDialog
from backend.data_managers.data_manager import DataManager

class MasteryDialog(QtWidgets.QDialog, AddMasteryDialog):
    def __init__(self, data_manager: DataManager = None):
        super().__init__()
        self.setupUi(self)
        self.data_manager = data_manager
        self.loadMasteries()

    def loadMasteries(self):
        self.mastery_combo.addItem(" ")
        self.mastery_combo.addItems(self.data_manager.getMasteries())
        self.checkWildcards()
        self.mastery_combo.currentTextChanged.connect(self.updateMasteryPowers)

    def checkWildcards(self):
        available_masteries = self.data_manager.getAvailableMasteries()
        for i in range(self.mastery_combo.count()):
            item = self.mastery_combo.model().item(i)
            if item.text() != " " and not available_masteries[item.text()]:
                item.setEnabled(False)

    def updateMasteryPowers(self):
        mastery = self.mastery_combo.currentText()
        mastery_object = self.data_manager.getMastery(mastery)
        first = True
        for power in mastery_object.powers:
            formated_power = self.data_manager.getPower(power).formatForDisplay()
            if first:
                self.power_1_name.setText(formated_power["name"])
                self.power_1_rules.setText(formated_power["rules"])
                self.power_1_qualities.setText(formated_power["qualities"])
            else:
                self.power_2_name.setText(formated_power["name"])
                self.power_2_rules.setText(formated_power["rules"])
                self.power_2_qualities.setText(formated_power["qualities"])
            first = not first
        self.frame.adjustSize()
        self.frame_2.adjustSize()
        self.adjustSize()

    def getMastery(self):
        return self.mastery_combo.currentText()
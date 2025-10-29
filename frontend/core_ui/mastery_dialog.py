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
        self.mastery_combo.addItems(list(self.data_manager.CONFIG.MASTERIES.keys()))
        self.checkWildcards()
        self.mastery_combo.currentTextChanged.connect(self.updateMasteryPowers)

    def checkWildcards(self):
        if self.data_manager.squad.wildcard is not None:
            for i in range(self.mastery_combo.count()):
                item = self.mastery_combo.model().item(i)
                mastery_object = self.data_manager.CONFIG.MASTERIES[item.text()] if item.text() != " " else None
                if mastery_object is not None and mastery_object.type == self.data_manager.squad.wildcard.type:
                    item.setEnabled(False)

    def updateMasteryPowers(self):
        mastery = self.mastery_combo.currentText()
        mastery_object = self.data_manager.CONFIG.MASTERIES[mastery]
        first = True
        for power in mastery_object.powers:
            power_object = self.data_manager.CONFIG.MASTERY_POWERS[power]
            name = power_object.name
            rules = power_object.rules
            qualities_text = "SP Cost: "
            qualities_text += "-" if power_object.sp_cost == 0 else str(power_object.sp_cost)
            qualities_text += " Epic: "
            qualities_text += "Yes" if power_object.is_epic else "No"
            qualities_text += " Passive: "
            qualities_text += "Yes" if power_object.is_passive else "No"
            if first:
                self.power_1_name.setText(name)
                self.power_1_rules.setText(rules)
                self.power_1_qualities.setText(qualities_text)
            else:
                self.power_2_name.setText(name)
                self.power_2_rules.setText(rules)
                self.power_2_qualities.setText(qualities_text)
            first = not first
        self.frame.adjustSize()
        self.frame_2.adjustSize()
        self.adjustSize()

    def getMastery(self):
        return self.mastery_combo.currentText()
from PySide6 import QtWidgets
from frontend.generated_ui.leadership import Ui_Leadership as AddLeadershipDialog
from backend.data_managers.data_manager import DataManager

class LeadershipDialog(QtWidgets.QDialog, AddLeadershipDialog):
    def __init__(self, data_manager: DataManager = None):
        super().__init__()
        self.setupUi(self)
        self.data_manager = data_manager
        self.setupComboBox()

    def getAbility(self):
        return self.leader_ability_combo.currentText()
    
    def setupComboBox(self):
        self.leader_ability_combo.addItem(" ")
        self.leader_ability_combo.addItems(self.data_manager.LEADERSHIP_ABILITIES.keys())
        self.leader_ability_combo.currentTextChanged.connect(self.updateAbility)

    def updateAbility(self):
        try:
            self.rules_text.setText(self.data_manager.CONFIG.ABILITIES[
            self.data_manager.LEADERSHIP_ABILITIES[self.leader_ability_combo.currentText()].abilities[0]].rules)
        except:
            self.rules_text.setText("")


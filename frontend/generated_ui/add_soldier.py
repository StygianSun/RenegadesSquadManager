# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addsoldier.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractScrollArea, QApplication,
    QCheckBox, QComboBox, QDialog, QDialogButtonBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AddSoldier(object):
    def setupUi(self, AddSoldier):
        if not AddSoldier.objectName():
            AddSoldier.setObjectName(u"AddSoldier")
        AddSoldier.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(AddSoldier.sizePolicy().hasHeightForWidth())
        AddSoldier.setSizePolicy(sizePolicy)
        AddSoldier.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(AddSoldier)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.soldier_label = QLabel(AddSoldier)
        self.soldier_label.setObjectName(u"soldier_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.soldier_label.sizePolicy().hasHeightForWidth())
        self.soldier_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.soldier_label)

        self.soldier_name = QTextEdit(AddSoldier)
        self.soldier_name.setObjectName(u"soldier_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.soldier_name.sizePolicy().hasHeightForWidth())
        self.soldier_name.setSizePolicy(sizePolicy2)
        self.soldier_name.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.soldier_name)

        self.soldier_type_label = QLabel(AddSoldier)
        self.soldier_type_label.setObjectName(u"soldier_type_label")
        sizePolicy1.setHeightForWidth(self.soldier_type_label.sizePolicy().hasHeightForWidth())
        self.soldier_type_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.soldier_type_label)

        self.soldier_type_combo = QComboBox(AddSoldier)
        self.soldier_type_combo.setObjectName(u"soldier_type_combo")
        sizePolicy2.setHeightForWidth(self.soldier_type_combo.sizePolicy().hasHeightForWidth())
        self.soldier_type_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.soldier_type_combo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cost_label = QLabel(AddSoldier)
        self.cost_label.setObjectName(u"cost_label")
        sizePolicy1.setHeightForWidth(self.cost_label.sizePolicy().hasHeightForWidth())
        self.cost_label.setSizePolicy(sizePolicy1)
        self.cost_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.cost_label)

        self.cost_text = QLabel(AddSoldier)
        self.cost_text.setObjectName(u"cost_text")
        sizePolicy2.setHeightForWidth(self.cost_text.sizePolicy().hasHeightForWidth())
        self.cost_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.cost_text)

        self.vitality_label = QLabel(AddSoldier)
        self.vitality_label.setObjectName(u"vitality_label")
        sizePolicy1.setHeightForWidth(self.vitality_label.sizePolicy().hasHeightForWidth())
        self.vitality_label.setSizePolicy(sizePolicy1)
        self.vitality_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.vitality_label)

        self.vitality_text = QLabel(AddSoldier)
        self.vitality_text.setObjectName(u"vitality_text")
        sizePolicy2.setHeightForWidth(self.vitality_text.sizePolicy().hasHeightForWidth())
        self.vitality_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.vitality_text)

        self.slots_label = QLabel(AddSoldier)
        self.slots_label.setObjectName(u"slots_label")
        sizePolicy1.setHeightForWidth(self.slots_label.sizePolicy().hasHeightForWidth())
        self.slots_label.setSizePolicy(sizePolicy1)
        self.slots_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.slots_label)

        self.slots_text = QLabel(AddSoldier)
        self.slots_text.setObjectName(u"slots_text")
        sizePolicy2.setHeightForWidth(self.slots_text.sizePolicy().hasHeightForWidth())
        self.slots_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.slots_text)

        self.ap_label = QLabel(AddSoldier)
        self.ap_label.setObjectName(u"ap_label")
        sizePolicy1.setHeightForWidth(self.ap_label.sizePolicy().hasHeightForWidth())
        self.ap_label.setSizePolicy(sizePolicy1)
        self.ap_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.ap_label)

        self.ap_text = QLabel(AddSoldier)
        self.ap_text.setObjectName(u"ap_text")
        sizePolicy2.setHeightForWidth(self.ap_text.sizePolicy().hasHeightForWidth())
        self.ap_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_7.addWidget(self.ap_text)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rarity_label = QLabel(AddSoldier)
        self.rarity_label.setObjectName(u"rarity_label")
        sizePolicy1.setHeightForWidth(self.rarity_label.sizePolicy().hasHeightForWidth())
        self.rarity_label.setSizePolicy(sizePolicy1)
        self.rarity_label.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_8.addWidget(self.rarity_label)

        self.rarity_text = QLabel(AddSoldier)
        self.rarity_text.setObjectName(u"rarity_text")
        sizePolicy2.setHeightForWidth(self.rarity_text.sizePolicy().hasHeightForWidth())
        self.rarity_text.setSizePolicy(sizePolicy2)
        self.rarity_text.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_8.addWidget(self.rarity_text)

        self.move_label = QLabel(AddSoldier)
        self.move_label.setObjectName(u"move_label")
        sizePolicy1.setHeightForWidth(self.move_label.sizePolicy().hasHeightForWidth())
        self.move_label.setSizePolicy(sizePolicy1)
        self.move_label.setMaximumSize(QSize(60, 16777215))
        self.move_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.move_label)

        self.move_text = QLabel(AddSoldier)
        self.move_text.setObjectName(u"move_text")
        sizePolicy2.setHeightForWidth(self.move_text.sizePolicy().hasHeightForWidth())
        self.move_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.move_text)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, -1)
        self.abilities_label = QLabel(AddSoldier)
        self.abilities_label.setObjectName(u"abilities_label")
        sizePolicy1.setHeightForWidth(self.abilities_label.sizePolicy().hasHeightForWidth())
        self.abilities_label.setSizePolicy(sizePolicy1)
        self.abilities_label.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout_5.addWidget(self.abilities_label)

        self.abilities_text = QLabel(AddSoldier)
        self.abilities_text.setObjectName(u"abilities_text")
        sizePolicy2.setHeightForWidth(self.abilities_text.sizePolicy().hasHeightForWidth())
        self.abilities_text.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.abilities_text)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.upgrades_label = QLabel(AddSoldier)
        self.upgrades_label.setObjectName(u"upgrades_label")
        sizePolicy1.setHeightForWidth(self.upgrades_label.sizePolicy().hasHeightForWidth())
        self.upgrades_label.setSizePolicy(sizePolicy1)
        self.upgrades_label.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_3.addWidget(self.upgrades_label)

        self.upgrades_tree = QTreeWidget(AddSoldier)
        self.upgrades_tree.setObjectName(u"upgrades_tree")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.upgrades_tree.sizePolicy().hasHeightForWidth())
        self.upgrades_tree.setSizePolicy(sizePolicy3)
        self.upgrades_tree.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.upgrades_tree.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.upgrades_tree.setAlternatingRowColors(True)
        self.upgrades_tree.setItemsExpandable(True)
        self.upgrades_tree.setHeaderHidden(False)
        self.upgrades_tree.setExpandsOnDoubleClick(False)
        self.upgrades_tree.setColumnCount(3)
        self.upgrades_tree.header().setCascadingSectionResizes(False)
        self.upgrades_tree.header().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.upgrades_tree)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.add_equipment_button = QPushButton(AddSoldier)
        self.add_equipment_button.setObjectName(u"add_equipment_button")
        sizePolicy1.setHeightForWidth(self.add_equipment_button.sizePolicy().hasHeightForWidth())
        self.add_equipment_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.add_equipment_button)

        self.equipment_type_combo = QComboBox(AddSoldier)
        self.equipment_type_combo.setObjectName(u"equipment_type_combo")
        sizePolicy2.setHeightForWidth(self.equipment_type_combo.sizePolicy().hasHeightForWidth())
        self.equipment_type_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.equipment_type_combo)

        self.equipment_combo = QComboBox(AddSoldier)
        self.equipment_combo.setObjectName(u"equipment_combo")
        sizePolicy2.setHeightForWidth(self.equipment_combo.sizePolicy().hasHeightForWidth())
        self.equipment_combo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.equipment_combo)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.equipped_items_label = QLabel(AddSoldier)
        self.equipped_items_label.setObjectName(u"equipped_items_label")
        sizePolicy1.setHeightForWidth(self.equipped_items_label.sizePolicy().hasHeightForWidth())
        self.equipped_items_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.equipped_items_label)

        self.equipped_items_table = QTableWidget(AddSoldier)
        if (self.equipped_items_table.columnCount() < 6):
            self.equipped_items_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.equipped_items_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.equipped_items_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.equipped_items_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.equipped_items_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.equipped_items_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.equipped_items_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.equipped_items_table.setObjectName(u"equipped_items_table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.equipped_items_table.sizePolicy().hasHeightForWidth())
        self.equipped_items_table.setSizePolicy(sizePolicy4)
        self.equipped_items_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.equipped_items_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.equipped_items_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.equipped_items_table.setProperty(u"showDropIndicator", False)
        self.equipped_items_table.setDragDropOverwriteMode(False)
        self.equipped_items_table.horizontalHeader().setVisible(True)
        self.equipped_items_table.horizontalHeader().setCascadingSectionResizes(True)
        self.equipped_items_table.verticalHeader().setVisible(True)
        self.equipped_items_table.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_10.addWidget(self.equipped_items_table)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.is_leader_checkbox = QCheckBox(AddSoldier)
        self.is_leader_checkbox.setObjectName(u"is_leader_checkbox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.is_leader_checkbox.sizePolicy().hasHeightForWidth())
        self.is_leader_checkbox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.is_leader_checkbox)

        self.leader_bonus_label = QLabel(AddSoldier)
        self.leader_bonus_label.setObjectName(u"leader_bonus_label")
        sizePolicy5.setHeightForWidth(self.leader_bonus_label.sizePolicy().hasHeightForWidth())
        self.leader_bonus_label.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.leader_bonus_label)

        self.leader_bonus_text = QLabel(AddSoldier)
        self.leader_bonus_text.setObjectName(u"leader_bonus_text")
        sizePolicy5.setHeightForWidth(self.leader_bonus_text.sizePolicy().hasHeightForWidth())
        self.leader_bonus_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.leader_bonus_text)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.is_psymancer_checkbox = QCheckBox(AddSoldier)
        self.is_psymancer_checkbox.setObjectName(u"is_psymancer_checkbox")
        sizePolicy1.setHeightForWidth(self.is_psymancer_checkbox.sizePolicy().hasHeightForWidth())
        self.is_psymancer_checkbox.setSizePolicy(sizePolicy1)
        self.is_psymancer_checkbox.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_12.addWidget(self.is_psymancer_checkbox)

        self.psymancer_type_text = QLabel(AddSoldier)
        self.psymancer_type_text.setObjectName(u"psymancer_type_text")
        sizePolicy5.setHeightForWidth(self.psymancer_type_text.sizePolicy().hasHeightForWidth())
        self.psymancer_type_text.setSizePolicy(sizePolicy5)
        self.psymancer_type_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.psymancer_type_text)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.psychic_powers_label = QLabel(AddSoldier)
        self.psychic_powers_label.setObjectName(u"psychic_powers_label")
        sizePolicy1.setHeightForWidth(self.psychic_powers_label.sizePolicy().hasHeightForWidth())
        self.psychic_powers_label.setSizePolicy(sizePolicy1)
        self.psychic_powers_label.setMaximumSize(QSize(100, 16777215))
        self.psychic_powers_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.psychic_powers_label)

        self.psychic_powers_text = QLabel(AddSoldier)
        self.psychic_powers_text.setObjectName(u"psychic_powers_text")
        sizePolicy5.setHeightForWidth(self.psychic_powers_text.sizePolicy().hasHeightForWidth())
        self.psychic_powers_text.setSizePolicy(sizePolicy5)

        self.horizontalLayout_13.addWidget(self.psychic_powers_text)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.buttonBox = QDialogButtonBox(AddSoldier)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy6)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddSoldier)
        self.buttonBox.accepted.connect(AddSoldier.accept)
        self.buttonBox.rejected.connect(AddSoldier.reject)

        QMetaObject.connectSlotsByName(AddSoldier)
    # setupUi

    def retranslateUi(self, AddSoldier):
        AddSoldier.setWindowTitle(QCoreApplication.translate("AddSoldier", u"Add Soldier", None))
        self.soldier_label.setText(QCoreApplication.translate("AddSoldier", u"Soldier Name:", None))
        self.soldier_type_label.setText(QCoreApplication.translate("AddSoldier", u"Soldier Type:", None))
        self.cost_label.setText(QCoreApplication.translate("AddSoldier", u"Cost:", None))
        self.cost_text.setText(QCoreApplication.translate("AddSoldier", u"0", None))
        self.vitality_label.setText(QCoreApplication.translate("AddSoldier", u"Vitality:", None))
        self.vitality_text.setText(QCoreApplication.translate("AddSoldier", u"0", None))
        self.slots_label.setText(QCoreApplication.translate("AddSoldier", u"Slots:", None))
        self.slots_text.setText(QCoreApplication.translate("AddSoldier", u"0", None))
        self.ap_label.setText(QCoreApplication.translate("AddSoldier", u"AP:", None))
        self.ap_text.setText(QCoreApplication.translate("AddSoldier", u"0", None))
        self.rarity_label.setText(QCoreApplication.translate("AddSoldier", u"Rarity:", None))
        self.rarity_text.setText("")
        self.move_label.setText(QCoreApplication.translate("AddSoldier", u"Movement:", None))
        self.move_text.setText(QCoreApplication.translate("AddSoldier", u"0\" + D0 Normal", None))
        self.abilities_label.setText(QCoreApplication.translate("AddSoldier", u"Abilities:", None))
        self.abilities_text.setText("")
        self.upgrades_label.setText(QCoreApplication.translate("AddSoldier", u"Upgrades:", None))
        ___qtreewidgetitem = self.upgrades_tree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("AddSoldier", u"Rarity", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("AddSoldier", u"Cost", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AddSoldier", u"Upgrade", None));
        self.add_equipment_button.setText(QCoreApplication.translate("AddSoldier", u"Add Equipment", None))
        self.equipped_items_label.setText(QCoreApplication.translate("AddSoldier", u"Equipped Items:", None))
        ___qtablewidgetitem = self.equipped_items_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddSoldier", u"Name", None));
        ___qtablewidgetitem1 = self.equipped_items_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddSoldier", u"Cost", None));
        ___qtablewidgetitem2 = self.equipped_items_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddSoldier", u"Rarity", None));
        ___qtablewidgetitem3 = self.equipped_items_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddSoldier", u"Range", None));
        ___qtablewidgetitem4 = self.equipped_items_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddSoldier", u"Attack Dice", None));
        ___qtablewidgetitem5 = self.equipped_items_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddSoldier", u"Damage", None));
        self.is_leader_checkbox.setText(QCoreApplication.translate("AddSoldier", u"Promote to Leader", None))
        self.leader_bonus_label.setText(QCoreApplication.translate("AddSoldier", u"Leadership Bonus:", None))
        self.leader_bonus_text.setText("")
        self.is_psymancer_checkbox.setText(QCoreApplication.translate("AddSoldier", u"Train Psymancer", None))
        self.psymancer_type_text.setText("")
        self.psychic_powers_label.setText(QCoreApplication.translate("AddSoldier", u"Psychic Powers:", None))
        self.psychic_powers_text.setText("")
    # retranslateUi


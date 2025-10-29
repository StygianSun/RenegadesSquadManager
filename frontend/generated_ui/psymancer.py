# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'psymancer.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Psymancer(object):
    def setupUi(self, Psymancer):
        if not Psymancer.objectName():
            Psymancer.setObjectName(u"Psymancer")
        Psymancer.resize(300, 200)
        self.verticalLayout = QVBoxLayout(Psymancer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.grade_label = QLabel(Psymancer)
        self.grade_label.setObjectName(u"grade_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grade_label.sizePolicy().hasHeightForWidth())
        self.grade_label.setSizePolicy(sizePolicy)
        self.grade_label.setMaximumSize(QSize(100, 30))
        self.grade_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.grade_label)

        self.grade_combo_box = QComboBox(Psymancer)
        self.grade_combo_box.setObjectName(u"grade_combo_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.grade_combo_box.sizePolicy().hasHeightForWidth())
        self.grade_combo_box.setSizePolicy(sizePolicy1)
        self.grade_combo_box.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.grade_combo_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.power_1_combo = QComboBox(Psymancer)
        self.power_1_combo.setObjectName(u"power_1_combo")
        self.power_1_combo.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.power_1_combo.sizePolicy().hasHeightForWidth())
        self.power_1_combo.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.power_1_combo)

        self.power_2_combo = QComboBox(Psymancer)
        self.power_2_combo.setObjectName(u"power_2_combo")
        self.power_2_combo.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.power_2_combo.sizePolicy().hasHeightForWidth())
        self.power_2_combo.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.power_2_combo)

        self.power_3_combo = QComboBox(Psymancer)
        self.power_3_combo.setObjectName(u"power_3_combo")
        self.power_3_combo.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.power_3_combo.sizePolicy().hasHeightForWidth())
        self.power_3_combo.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.power_3_combo)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(Psymancer)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Psymancer)
        self.buttonBox.accepted.connect(Psymancer.accept)
        self.buttonBox.rejected.connect(Psymancer.reject)

        QMetaObject.connectSlotsByName(Psymancer)
    # setupUi

    def retranslateUi(self, Psymancer):
        Psymancer.setWindowTitle(QCoreApplication.translate("Psymancer", u"Train a Psymancer", None))
        self.grade_label.setText(QCoreApplication.translate("Psymancer", u"Psymancer Grade:", None))
    # retranslateUi


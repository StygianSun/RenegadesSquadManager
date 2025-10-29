# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addmastery.ui'
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
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddMastery(object):
    def setupUi(self, AddMastery):
        if not AddMastery.objectName():
            AddMastery.setObjectName(u"AddMastery")
        AddMastery.resize(276, 276)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddMastery.sizePolicy().hasHeightForWidth())
        AddMastery.setSizePolicy(sizePolicy)
        AddMastery.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(AddMastery)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.mastery_label = QLabel(AddMastery)
        self.mastery_label.setObjectName(u"mastery_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mastery_label.sizePolicy().hasHeightForWidth())
        self.mastery_label.setSizePolicy(sizePolicy1)
        self.mastery_label.setMaximumSize(QSize(50, 16777215))
        self.mastery_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.mastery_label)

        self.mastery_combo = QComboBox(AddMastery)
        self.mastery_combo.setObjectName(u"mastery_combo")

        self.horizontalLayout_2.addWidget(self.mastery_combo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.frame = QFrame(AddMastery)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.power_2_name = QLabel(self.frame)
        self.power_2_name.setObjectName(u"power_2_name")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.power_2_name.sizePolicy().hasHeightForWidth())
        self.power_2_name.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.power_2_name)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.power_2_rules = QLabel(self.frame)
        self.power_2_rules.setObjectName(u"power_2_rules")
        sizePolicy2.setHeightForWidth(self.power_2_rules.sizePolicy().hasHeightForWidth())
        self.power_2_rules.setSizePolicy(sizePolicy2)
        self.power_2_rules.setMaximumSize(QSize(400, 16777215))
        self.power_2_rules.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.power_2_rules.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.power_2_rules)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.power_2_qualities = QLabel(self.frame)
        self.power_2_qualities.setObjectName(u"power_2_qualities")
        sizePolicy2.setHeightForWidth(self.power_2_qualities.sizePolicy().hasHeightForWidth())
        self.power_2_qualities.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.power_2_qualities)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(AddMastery)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.power_1_name = QLabel(self.frame_2)
        self.power_1_name.setObjectName(u"power_1_name")
        sizePolicy3.setHeightForWidth(self.power_1_name.sizePolicy().hasHeightForWidth())
        self.power_1_name.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.power_1_name)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.power_1_rules = QLabel(self.frame_2)
        self.power_1_rules.setObjectName(u"power_1_rules")
        sizePolicy2.setHeightForWidth(self.power_1_rules.sizePolicy().hasHeightForWidth())
        self.power_1_rules.setSizePolicy(sizePolicy2)
        self.power_1_rules.setMaximumSize(QSize(400, 16777215))
        self.power_1_rules.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.power_1_rules.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.power_1_rules)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.power_1_qualities = QLabel(self.frame_2)
        self.power_1_qualities.setObjectName(u"power_1_qualities")
        sizePolicy2.setHeightForWidth(self.power_1_qualities.sizePolicy().hasHeightForWidth())
        self.power_1_qualities.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.power_1_qualities)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.buttonBox = QDialogButtonBox(AddMastery)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddMastery)
        self.buttonBox.accepted.connect(AddMastery.accept)
        self.buttonBox.rejected.connect(AddMastery.reject)

        QMetaObject.connectSlotsByName(AddMastery)
    # setupUi

    def retranslateUi(self, AddMastery):
        AddMastery.setWindowTitle(QCoreApplication.translate("AddMastery", u"Add Mastery", None))
        self.mastery_label.setText(QCoreApplication.translate("AddMastery", u"Mastery:", None))
        self.power_2_name.setText("")
        self.power_2_rules.setText("")
        self.power_2_qualities.setText("")
        self.power_1_name.setText("")
        self.power_1_rules.setText("")
        self.power_1_qualities.setText("")
    # retranslateUi


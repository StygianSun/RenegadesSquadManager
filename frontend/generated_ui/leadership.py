# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leadership.ui'
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
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Leadership(object):
    def setupUi(self, Leadership):
        if not Leadership.objectName():
            Leadership.setObjectName(u"Leadership")
        Leadership.resize(300, 200)
        self.verticalLayout = QVBoxLayout(Leadership)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leader_ability_combo = QComboBox(Leadership)
        self.leader_ability_combo.setObjectName(u"leader_ability_combo")
        self.leader_ability_combo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.leader_ability_combo.setMaxVisibleItems(15)

        self.verticalLayout.addWidget(self.leader_ability_combo)

        self.rules_text = QLabel(Leadership)
        self.rules_text.setObjectName(u"rules_text")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rules_text.sizePolicy().hasHeightForWidth())
        self.rules_text.setSizePolicy(sizePolicy)
        self.rules_text.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.rules_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.rules_text)

        self.buttonBox = QDialogButtonBox(Leadership)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Leadership)
        self.buttonBox.accepted.connect(Leadership.accept)
        self.buttonBox.rejected.connect(Leadership.reject)

        QMetaObject.connectSlotsByName(Leadership)
    # setupUi

    def retranslateUi(self, Leadership):
        Leadership.setWindowTitle(QCoreApplication.translate("Leadership", u"Dialog", None))
        self.rules_text.setText("")
    # retranslateUi


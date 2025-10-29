# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionNew_Squad = QAction(MainWindow)
        self.actionNew_Squad.setObjectName(u"actionNew_Squad")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.actionNew_Squad.setIcon(icon)
        self.actionNew_Squad.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionSave_Squad = QAction(MainWindow)
        self.actionSave_Squad.setObjectName(u"actionSave_Squad")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave_Squad.setIcon(icon1)
        self.actionSave_Squad.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionLoad_Squad = QAction(MainWindow)
        self.actionLoad_Squad.setObjectName(u"actionLoad_Squad")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionLoad_Squad.setIcon(icon2)
        self.actionLoad_Squad.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionGenerate_PDF = QAction(MainWindow)
        self.actionGenerate_PDF.setObjectName(u"actionGenerate_PDF")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditCopy))
        self.actionGenerate_PDF.setIcon(icon3)
        self.actionGenerate_PDF.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.actionSave_Squad_As = QAction(MainWindow)
        self.actionSave_Squad_As.setObjectName(u"actionSave_Squad_As")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.actionSave_Squad_As.setIcon(icon4)
        self.actionSave_Squad_As.setMenuRole(QAction.MenuRole.ApplicationSpecificRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.player_label = QLabel(self.centralwidget)
        self.player_label.setObjectName(u"player_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.player_label.sizePolicy().hasHeightForWidth())
        self.player_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.player_label)

        self.player_name = QLineEdit(self.centralwidget)
        self.player_name.setObjectName(u"player_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.player_name.sizePolicy().hasHeightForWidth())
        self.player_name.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.player_name)

        self.squad_label = QLabel(self.centralwidget)
        self.squad_label.setObjectName(u"squad_label")
        sizePolicy1.setHeightForWidth(self.squad_label.sizePolicy().hasHeightForWidth())
        self.squad_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.squad_label)

        self.squad_name = QLineEdit(self.centralwidget)
        self.squad_name.setObjectName(u"squad_name")
        sizePolicy2.setHeightForWidth(self.squad_name.sizePolicy().hasHeightForWidth())
        self.squad_name.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.squad_name)

        self.total_cost_label = QLabel(self.centralwidget)
        self.total_cost_label.setObjectName(u"total_cost_label")
        sizePolicy1.setHeightForWidth(self.total_cost_label.sizePolicy().hasHeightForWidth())
        self.total_cost_label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.total_cost_label)

        self.total_cost_text = QLabel(self.centralwidget)
        self.total_cost_text.setObjectName(u"total_cost_text")
        sizePolicy1.setHeightForWidth(self.total_cost_text.sizePolicy().hasHeightForWidth())
        self.total_cost_text.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.total_cost_text)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.add_soldier_button = QPushButton(self.centralwidget)
        self.add_soldier_button.setObjectName(u"add_soldier_button")
        self.add_soldier_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.add_soldier_button.sizePolicy().hasHeightForWidth())
        self.add_soldier_button.setSizePolicy(sizePolicy1)
        self.add_soldier_button.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.add_soldier_button, 0, Qt.AlignmentFlag.AlignTop)

        self.squad_members_table = QTableWidget(self.centralwidget)
        if (self.squad_members_table.columnCount() < 7):
            self.squad_members_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.squad_members_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.squad_members_table.setObjectName(u"squad_members_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.squad_members_table.sizePolicy().hasHeightForWidth())
        self.squad_members_table.setSizePolicy(sizePolicy3)
        self.squad_members_table.setMinimumSize(QSize(0, 150))
        self.squad_members_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.squad_members_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.squad_members_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.squad_members_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.squad_members_table.setDragDropOverwriteMode(False)
        self.squad_members_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.squad_members_table.setCornerButtonEnabled(False)
        self.squad_members_table.verticalHeader().setVisible(True)
        self.squad_members_table.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_2.addWidget(self.squad_members_table)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.add_mastery_button = QPushButton(self.centralwidget)
        self.add_mastery_button.setObjectName(u"add_mastery_button")
        self.add_mastery_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.add_mastery_button.sizePolicy().hasHeightForWidth())
        self.add_mastery_button.setSizePolicy(sizePolicy1)
        self.add_mastery_button.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_3.addWidget(self.add_mastery_button, 0, Qt.AlignmentFlag.AlignTop)

        self.squad_mastery_table = QTableWidget(self.centralwidget)
        if (self.squad_mastery_table.columnCount() < 3):
            self.squad_mastery_table.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.squad_mastery_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.squad_mastery_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.squad_mastery_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.squad_mastery_table.setObjectName(u"squad_mastery_table")
        sizePolicy3.setHeightForWidth(self.squad_mastery_table.sizePolicy().hasHeightForWidth())
        self.squad_mastery_table.setSizePolicy(sizePolicy3)
        self.squad_mastery_table.setMinimumSize(QSize(0, 150))
        self.squad_mastery_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.squad_mastery_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.squad_mastery_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.squad_mastery_table.setDragDropOverwriteMode(False)
        self.squad_mastery_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.squad_mastery_table.setCornerButtonEnabled(False)
        self.squad_mastery_table.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_3.addWidget(self.squad_mastery_table)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.rares_label = QLabel(self.centralwidget)
        self.rares_label.setObjectName(u"rares_label")
        sizePolicy1.setHeightForWidth(self.rares_label.sizePolicy().hasHeightForWidth())
        self.rares_label.setSizePolicy(sizePolicy1)
        self.rares_label.setMinimumSize(QSize(80, 0))
        self.rares_label.setMaximumSize(QSize(16777215, 120))

        self.horizontalLayout_9.addWidget(self.rares_label, 0, Qt.AlignmentFlag.AlignTop)

        self.rares_table = QTableWidget(self.centralwidget)
        if (self.rares_table.columnCount() < 2):
            self.rares_table.setColumnCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.rares_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.rares_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        self.rares_table.setObjectName(u"rares_table")
        sizePolicy3.setHeightForWidth(self.rares_table.sizePolicy().hasHeightForWidth())
        self.rares_table.setSizePolicy(sizePolicy3)
        self.rares_table.setMinimumSize(QSize(0, 150))
        self.rares_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.rares_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.rares_table.setDragDropOverwriteMode(False)
        self.rares_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.rares_table.setCornerButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.rares_table)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 627, 17))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionNew_Squad)
        self.menuFile.addAction(self.actionSave_Squad)
        self.menuFile.addAction(self.actionSave_Squad_As)
        self.menuFile.addAction(self.actionLoad_Squad)
        self.menuFile.addAction(self.actionGenerate_PDF)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Renegades Squad Manager", None))
        self.actionNew_Squad.setText(QCoreApplication.translate("MainWindow", u"New Squad", None))
        self.actionSave_Squad.setText(QCoreApplication.translate("MainWindow", u"Save Squad", None))
        self.actionLoad_Squad.setText(QCoreApplication.translate("MainWindow", u"Load Squad", None))
        self.actionGenerate_PDF.setText(QCoreApplication.translate("MainWindow", u"Generate PDF", None))
        self.actionSave_Squad_As.setText(QCoreApplication.translate("MainWindow", u"Save Squad As", None))
        self.player_label.setText(QCoreApplication.translate("MainWindow", u"Player:", None))
        self.squad_label.setText(QCoreApplication.translate("MainWindow", u"Squad:", None))
        self.total_cost_label.setText(QCoreApplication.translate("MainWindow", u"Total Cost:", None))
        self.total_cost_text.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.add_soldier_button.setText(QCoreApplication.translate("MainWindow", u"Add Soldier", None))
        ___qtablewidgetitem = self.squad_members_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.squad_members_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.squad_members_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Is Leader", None));
        ___qtablewidgetitem3 = self.squad_members_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Is Psymancer", None));
        ___qtablewidgetitem4 = self.squad_members_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        ___qtablewidgetitem5 = self.squad_members_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Upgrades", None));
        ___qtablewidgetitem6 = self.squad_members_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Equipment", None));
        self.add_mastery_button.setText(QCoreApplication.translate("MainWindow", u"Add Mastery", None))
        ___qtablewidgetitem7 = self.squad_mastery_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Mastery", None));
        ___qtablewidgetitem8 = self.squad_mastery_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem9 = self.squad_mastery_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Powers", None));
        self.rares_label.setText(QCoreApplication.translate("MainWindow", u"Rares:", None))
        ___qtablewidgetitem10 = self.rares_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem11 = self.rares_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Rare Cost", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File...", None))
    # retranslateUi


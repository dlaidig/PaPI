# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui/manager.ui'
#
# Created: Tue Sep 16 12:07:50 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Manager(object):
    def setupUi(self, Manager):
        Manager.setObjectName("Manager")
        Manager.resize(792, 742)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Manager.sizePolicy().hasHeightForWidth())
        Manager.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(Manager)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QtCore.QSize(791, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 771, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treePlugin = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.treePlugin.setAnimated(True)
        self.treePlugin.setAllColumnsShowFocus(True)
        self.treePlugin.setObjectName("treePlugin")
        self.treePlugin.header().setVisible(True)
        self.treePlugin.header().setCascadingSectionResizes(False)
        self.treePlugin.header().setDefaultSectionSize(100)
        self.treePlugin.header().setHighlightSections(True)
        self.treePlugin.header().setMinimumSectionSize(30)
        self.treePlugin.header().setSortIndicatorShown(True)
        self.treePlugin.header().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.treePlugin)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.le_ID = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.le_ID.setReadOnly(True)
        self.le_ID.setObjectName("le_ID")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_ID)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.le_Type = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.le_Type.setReadOnly(True)
        self.le_Type.setObjectName("le_Type")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.le_Type)
        self.le_Path = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.le_Path.setEnabled(True)
        self.le_Path.setReadOnly(True)
        self.le_Path.setObjectName("le_Path")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.le_Path)
        self.verticalLayout.addLayout(self.formLayout)
        self.tableParameter = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tableParameter.setRowCount(0)
        self.tableParameter.setColumnCount(3)
        self.tableParameter.setObjectName("tableParameter")
        self.tableParameter.setColumnCount(3)
        self.tableParameter.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableParameter.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableParameter.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableParameter.setHorizontalHeaderItem(2, item)
        self.tableParameter.horizontalHeader().setDefaultSectionSize(100)
        self.verticalLayout.addWidget(self.tableParameter)
        self.treeBlock = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.treeBlock.setObjectName("treeBlock")
        self.treeBlock.header().setDefaultSectionSize(80)
        self.verticalLayout.addWidget(self.treeBlock)
        self.treeSignal = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.treeSignal.setObjectName("treeSignal")
        self.verticalLayout.addWidget(self.treeSignal)
        self.horizontalLayout.addLayout(self.verticalLayout)
        Manager.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Manager)
        self.statusbar.setObjectName("statusbar")
        Manager.setStatusBar(self.statusbar)

        self.retranslateUi(Manager)
        QtCore.QMetaObject.connectSlotsByName(Manager)

    def retranslateUi(self, Manager):
        Manager.setWindowTitle(QtGui.QApplication.translate("Manager", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treePlugin.setSortingEnabled(True)
        self.treePlugin.headerItem().setText(0, QtGui.QApplication.translate("Manager", "Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.treePlugin.headerItem().setText(1, QtGui.QApplication.translate("Manager", "#Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.treePlugin.headerItem().setText(2, QtGui.QApplication.translate("Manager", "#Blocks", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Manager", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Manager", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Manager", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.tableParameter.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Manager", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.tableParameter.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Manager", "PCP", None, QtGui.QApplication.UnicodeUTF8))
        self.tableParameter.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Manager", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.treeBlock.headerItem().setText(0, QtGui.QApplication.translate("Manager", "Block", None, QtGui.QApplication.UnicodeUTF8))
        self.treeBlock.headerItem().setText(1, QtGui.QApplication.translate("Manager", "Subscriber", None, QtGui.QApplication.UnicodeUTF8))
        self.treeSignal.headerItem().setText(0, QtGui.QApplication.translate("Manager", "Signal", None, QtGui.QApplication.UnicodeUTF8))


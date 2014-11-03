# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui/qt_new/main.ui'
#
# Created: Mon Nov  3 12:30:46 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QtNewMain(object):
    def setupUi(self, QtNewMain):
        QtNewMain.setObjectName("QtNewMain")
        QtNewMain.resize(693, 600)
        self.centralwidget = QtGui.QWidget(QtNewMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadButton = QtGui.QPushButton(self.centralwidget)
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widgetArea = QtGui.QMdiArea(self.centralwidget)
        self.widgetArea.setObjectName("widgetArea")
        self.verticalLayout.addWidget(self.widgetArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        QtNewMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QtNewMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 25))
        self.menubar.setObjectName("menubar")
        self.menuPaPI = QtGui.QMenu(self.menubar)
        self.menuPaPI.setObjectName("menuPaPI")
        self.menuPlugin = QtGui.QMenu(self.menubar)
        self.menuPlugin.setObjectName("menuPlugin")
        QtNewMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QtNewMain)
        self.statusbar.setObjectName("statusbar")
        QtNewMain.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(QtNewMain)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtGui.QAction(QtNewMain)
        self.actionSave.setObjectName("actionSave")
        self.actionOverview = QtGui.QAction(QtNewMain)
        self.actionOverview.setObjectName("actionOverview")
        self.actionCreate = QtGui.QAction(QtNewMain)
        self.actionCreate.setObjectName("actionCreate")
        self.actionExit = QtGui.QAction(QtNewMain)
        self.actionExit.setObjectName("actionExit")
        self.actionReloadConfig = QtGui.QAction(QtNewMain)
        self.actionReloadConfig.setObjectName("actionReloadConfig")
        self.actionResetPaPI = QtGui.QAction(QtNewMain)
        self.actionResetPaPI.setObjectName("actionResetPaPI")
        self.menuPaPI.addAction(self.actionLoad)
        self.menuPaPI.addAction(self.actionSave)
        self.menuPaPI.addAction(self.actionExit)
        self.menuPaPI.addAction(self.actionReloadConfig)
        self.menuPaPI.addAction(self.actionResetPaPI)
        self.menuPlugin.addAction(self.actionOverview)
        self.menuPlugin.addAction(self.actionCreate)
        self.menubar.addAction(self.menuPaPI.menuAction())
        self.menubar.addAction(self.menuPlugin.menuAction())

        self.retranslateUi(QtNewMain)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), QtNewMain.close)
        QtCore.QMetaObject.connectSlotsByName(QtNewMain)

    def retranslateUi(self, QtNewMain):
        QtNewMain.setWindowTitle(QtGui.QApplication.translate("QtNewMain", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("QtNewMain", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("QtNewMain", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPaPI.setTitle(QtGui.QApplication.translate("QtNewMain", "PaPI", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugin.setTitle(QtGui.QApplication.translate("QtNewMain", "Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("QtNewMain", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("QtNewMain", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOverview.setText(QtGui.QApplication.translate("QtNewMain", "Overview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCreate.setText(QtGui.QApplication.translate("QtNewMain", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("QtNewMain", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReloadConfig.setText(QtGui.QApplication.translate("QtNewMain", "ReloadConfig", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResetPaPI.setText(QtGui.QApplication.translate("QtNewMain", "ResetPaPI", None, QtGui.QApplication.UnicodeUTF8))


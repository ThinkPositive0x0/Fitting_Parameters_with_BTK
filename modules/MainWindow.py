# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(830, 320, 221, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeltaEdit_low = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.DeltaEdit_low.setText("")
        self.DeltaEdit_low.setObjectName("DeltaEdit_low")
        self.horizontalLayout.addWidget(self.DeltaEdit_low)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.DeltaEdit_high = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.DeltaEdit_high.setDragEnabled(True)
        self.DeltaEdit_high.setObjectName("DeltaEdit_high")
        self.horizontalLayout.addWidget(self.DeltaEdit_high)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GamaEdit_low = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.GamaEdit_low.setObjectName("GamaEdit_low")
        self.horizontalLayout_3.addWidget(self.GamaEdit_low)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.GamaEdit_high = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.GamaEdit_high.setObjectName("GamaEdit_high")
        self.horizontalLayout_3.addWidget(self.GamaEdit_high)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ZEdit_low = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ZEdit_low.setObjectName("ZEdit_low")
        self.horizontalLayout_4.addWidget(self.ZEdit_low)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.ZEdit_high = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ZEdit_high.setObjectName("ZEdit_high")
        self.horizontalLayout_4.addWidget(self.ZEdit_high)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PEdit_low = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.PEdit_low.setObjectName("PEdit_low")
        self.horizontalLayout_2.addWidget(self.PEdit_low)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.PEdit_high = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.PEdit_high.setObjectName("PEdit_high")
        self.horizontalLayout_2.addWidget(self.PEdit_high)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 340, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(780, 390, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 450, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 500, 21, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 240, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(920, 310, 51, 16))
        self.label_6.setObjectName("label_6")
        self.TempEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TempEdit.setGeometry(QtCore.QRect(910, 240, 89, 21))
        self.TempEdit.setObjectName("TempEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1010, 240, 31, 16))
        self.label_7.setObjectName("label_7")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 170, 711, 531))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(150, 50, 751, 89))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_file = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.add_file.setObjectName("add_file")
        self.horizontalLayout_5.addWidget(self.add_file)
        spacerItem4 = QtWidgets.QSpacerItem(48, 84, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.FileName = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.FileName.setObjectName("FileName")
        self.horizontalLayout_5.addWidget(self.FileName)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(900, 580, 93, 28))
        self.run.setObjectName("run")
        self.label_7.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.TempEdit.raise_()
        self.graphicsView.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.run.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 26))
        self.menubar.setObjectName("menubar")
        self.menuModified = QtWidgets.QMenu(self.menubar)
        self.menuModified.setObjectName("menuModified")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuModified.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Delta"))
        self.label_2.setText(_translate("MainWindow", "Gamma"))
        self.label_3.setText(_translate("MainWindow", "Z"))
        self.label_4.setText(_translate("MainWindow", "P"))
        self.label_5.setText(_translate("MainWindow", "Temperature"))
        self.label_6.setText(_translate("MainWindow", "Range"))
        self.label_7.setText(_translate("MainWindow", "(K)"))
        self.add_file.setText(_translate("MainWindow", "Add File"))
        self.run.setText(_translate("MainWindow", "Run"))
        self.menuModified.setTitle(_translate("MainWindow", "Modified BTK Fit"))



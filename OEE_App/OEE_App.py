# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OEE_App.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphWidget = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.graphWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphWidget.setObjectName("graphWidget")
        self.mplvl = QtWidgets.QVBoxLayout(self.graphWidget)
        self.mplvl.setObjectName("mplvl")
        self.horizontalLayout.addWidget(self.graphWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_dials = QtWidgets.QWidget()
        self.tab_dials.setObjectName("tab_dials")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_dials)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_dials)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_dials)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_dials)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.gauge_widget_4 = QtWidgets.QWidget(self.tab_dials)
        self.gauge_widget_4.setObjectName("gauge_widget_4")
        self.layout_gauge4 = QtWidgets.QVBoxLayout(self.gauge_widget_4)
        self.layout_gauge4.setObjectName("layout_gauge4")
        self.gridLayout_2.addWidget(self.gauge_widget_4, 1, 3, 1, 1)
        self.gauge_widget = QtWidgets.QWidget(self.tab_dials)
        self.gauge_widget.setObjectName("gauge_widget")
        self.layout_gauge1 = QtWidgets.QVBoxLayout(self.gauge_widget)
        self.layout_gauge1.setObjectName("layout_gauge1")
        self.gridLayout_2.addWidget(self.gauge_widget, 1, 0, 1, 1)
        self.gauge_widget_3 = QtWidgets.QWidget(self.tab_dials)
        self.gauge_widget_3.setObjectName("gauge_widget_3")
        self.layout_gauge3 = QtWidgets.QVBoxLayout(self.gauge_widget_3)
        self.layout_gauge3.setObjectName("layout_gauge3")
        self.gridLayout_2.addWidget(self.gauge_widget_3, 1, 2, 1, 1)
        self.gauge_widget_2 = QtWidgets.QWidget(self.tab_dials)
        self.gauge_widget_2.setObjectName("gauge_widget_2")
        self.layout_gauge2 = QtWidgets.QVBoxLayout(self.gauge_widget_2)
        self.layout_gauge2.setObjectName("layout_gauge2")
        self.gridLayout_2.addWidget(self.gauge_widget_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_dials)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_dials, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data"))
        self.label.setText(_translate("MainWindow", "OEE"))
        self.label_4.setText(_translate("MainWindow", "Quality"))
        self.label_3.setText(_translate("MainWindow", "Performance"))
        self.label_2.setText(_translate("MainWindow", "Availability"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dials), _translate("MainWindow", "Dials"))
        self.actionData.setText(_translate("MainWindow", "Data"))

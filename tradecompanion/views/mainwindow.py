# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/user/Documents/Code/PathOfExile/tradecompanion/views/mainwindow.ui',
# licensing of '/home/user/Documents/Code/PathOfExile/tradecompanion/views/mainwindow.ui' applies.
#
# Created: Sun Jul  7 19:55:26 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 300)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QWidget(self.centralwidget)
        self.title_bar.setStyleSheet("QWidget {background-color: white}")
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.transparency = QtWidgets.QSlider(self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transparency.sizePolicy().hasHeightForWidth())
        self.transparency.setSizePolicy(sizePolicy)
        self.transparency.setMaximum(95)
        self.transparency.setOrientation(QtCore.Qt.Horizontal)
        self.transparency.setObjectName("transparency")
        self.horizontalLayout.addWidget(self.transparency)
        self.title = QtWidgets.QLabel(self.title_bar)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.settings = QtWidgets.QPushButton(self.title_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.settings.setFont(font)
        self.settings.setFlat(True)
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.close = QtWidgets.QPushButton(self.title_bar)
        self.close.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.close.setFont(font)
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.title_bar)
        self.trades = QtWidgets.QTabWidget(self.centralwidget)
        self.trades.setTabPosition(QtWidgets.QTabWidget.South)
        self.trades.setUsesScrollButtons(True)
        self.trades.setTabsClosable(True)
        self.trades.setMovable(True)
        self.trades.setObjectName("trades")
        self.verticalLayout.addWidget(self.trades)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")

        self.retranslateUi(MainWindow)
        self.trades.setCurrentIndex(-1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Path of Exile Companion", None, -1))
        self.title.setText(QtWidgets.QApplication.translate("MainWindow", "Path of Exile Companion (0)", None, -1))
        self.settings.setText(QtWidgets.QApplication.translate("MainWindow", "⚙", None, -1))
        self.close.setText(QtWidgets.QApplication.translate("MainWindow", "×", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionPreferences.setText(QtWidgets.QApplication.translate("MainWindow", "Preferences...", None, -1))


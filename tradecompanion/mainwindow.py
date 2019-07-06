from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow

from tradecompanion.logparser import LogParser
from tradecompanion.tradewidget import TradeWidget
from tradecompanion.views.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, log_path):
        super().__init__()
        self.setWindowFlag(Qt.X11BypassWindowManagerHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.trades.tabCloseRequested.connect(self.on_tab_close_requested)

        self.log_monitor = LogParser(log_path)
        self.log_monitor.trade_request.connect(self.on_trade_request)
        self.log_monitor.start()

        self.is_dragging = False
        self.drag_position = self.pos()

    @QtCore.Slot()
    def on_close_clicked(self):
        self.close()

    @QtCore.Slot()
    def on_settings_clicked(self):
        print('Settings')

    def mousePressEvent(self, event):
        self.is_dragging = True
        self.drag_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.drag_position
        self.move(self.pos() + delta)
        self.drag_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.is_dragging = False

    def on_tab_close_requested(self, index):
        self.ui.trades.removeTab(index)

    def on_trade_request(self, data):
        trade_widget = TradeWidget(self, data)
        self.ui.trades.addTab(trade_widget, f'{self.ui.trades.count() + 1}')

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow

from tradecompanion.logmonitor import LogMonitor
from tradecompanion.tradewidget import TradeWidget
from tradecompanion.views.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, log_path):
        super().__init__()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.tabCloseRequested.connect(self.on_tab_close_requested)

        self.log_monitor = LogMonitor(log_path)
        self.log_monitor.trade_request.connect(self.on_trade_request)
        self.log_monitor.start()

    def on_tab_close_requested(self, index):
        self.ui.tabWidget.removeTab(index)

    def on_trade_request(self, data):
        trade_widget = TradeWidget(self, data)
        self.ui.tabWidget.addTab(trade_widget, str(self.ui.tabWidget.count() + 1))

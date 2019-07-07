from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QSizeGrip

from tradecompanion.logparser import LogParser
from tradecompanion.tradewidget import TradeWidget
from tradecompanion.views.mainwindow import Ui_MainWindow

TITLE_FORMAT = 'Path of Exile Companion ({})'


class MainWindow(QMainWindow):
    def __init__(self, log_path):
        super().__init__()
        self.setWindowFlag(Qt.X11BypassWindowManagerHint)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.size_grip = QSizeGrip(self)
        size_grip_height = self.size_grip.height()
        self.size_grip.setFixedSize(size_grip_height, size_grip_height)

        self.log_monitor = LogParser(log_path)
        self.log_monitor.trade_request.connect(self.on_trade_request)
        self.log_monitor.start()

        self.is_dragging = False
        self.drag_position = self.pos()

        self.update_title()

    def update_title(self):
        title = TITLE_FORMAT.format(self.ui.trades.count())
        self.setWindowTitle(title)
        self.ui.title.setText(title)

    @QtCore.Slot(int)
    def on_transparency_valueChanged(self, value):
        self.setWindowOpacity(1 - value / 100)

    @QtCore.Slot()
    def on_close_clicked(self):
        self.close()

    @QtCore.Slot()
    def on_settings_clicked(self):
        pass

    def on_trade_request(self, data):
        trade_widget = TradeWidget(self, data)
        self.ui.trades.addTab(trade_widget, str(self.ui.trades.count() + 1))
        self.update_title()

    @QtCore.Slot(int)
    def on_trades_tabCloseRequested(self, index):
        self.ui.trades.removeTab(index)
        self.update_title()

    def mousePressEvent(self, event):
        self.is_dragging = True
        self.drag_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.drag_position
        self.move(self.pos() + delta)
        self.drag_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.is_dragging = False

    def resizeEvent(self, event):
        position = self.size() - self.size_grip.size()
        self.size_grip.move(*position.toTuple())

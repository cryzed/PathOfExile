from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QWidget

from tradecompanion import xdotool
from tradecompanion.views.tradewidget import Ui_TradeWidget

WINDOW_TITLE_REGEX_PATTERN = r'Path of Exile$'


class TradeWidget(QWidget):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.ui = Ui_TradeWidget()
        self.ui.setupUi(self)

        self.data = data
        self.ui.buyer.setText(data['buyer'])
        self.ui.item.setText(data['item'])
        self.ui.price.setText(data['price'])
        self.ui.stash.setText(f'{data["league"]} (Tab: {data["stash"]} / Position: {data["left"]}/{data["top"]})')
        self.ui.other.setText(data['other'])
        self.ui.time.setText(self.data['time'].strftime('%H:%M:%S'))

    @QtCore.Slot()
    def on_copy_clicked(self):
        QApplication.clipboard().setText(self.data['item'])

    @QtCore.Slot()
    def on_whisper_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'@{self.data["buyer"]} ')

    @QtCore.Slot()
    def on_invite_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/invite {self.data["buyer"]}')
        xdotool.key(window_id, ['KP_Enter'])

    @QtCore.Slot()
    def on_trade_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/tradewith {self.data["buyer"]}')
        xdotool.key(window_id, ['KP_Enter'])

    @QtCore.Slot()
    def on_kick_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/kick {self.data["buyer"]}')
        xdotool.key(window_id, ['KP_Enter'])

    @QtCore.Slot()
    def on_thanks_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'@{self.data["buyer"]} Thanks!')
        xdotool.key(window_id, ['KP_Enter'])

        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/kick {self.data["buyer"]}')
        xdotool.key(window_id, ['KP_Enter'])

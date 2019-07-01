from PySide2 import QtCore
from PySide2.QtWidgets import QWidget, QApplication

from tradecompanion import xdotool
from tradecompanion.views.tradewidget import Ui_TradeWidget

WINDOW_TITLE_REGEX_PATTERN = r'Path of Exile$'


class TradeWidget(QWidget):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.ui = Ui_TradeWidget()
        self.ui.setupUi(self)

        self.data = data
        self.ui.buyer.setText(data['name'])
        self.ui.item.setText(data['item'])
        self.ui.price.setText(data['price'])
        self.ui.stash.setText(f'{data["league"]} (Tab: {data["stash_tab"]} / Position: {data["left"]}/{data["top"]})')
        self.ui.time.setText(self.data['time'].strftime('%H:%M:%S'))

    # TODO: Work in progress
    @QtCore.Slot()
    def on_copy_item_name_clicked(self):
        QApplication.clipboard().setText(self.data['item'])

    @QtCore.Slot()
    def on_whisper_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'@{self.data["name"]} ')

    @QtCore.Slot()
    def on_invite_to_party_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/invite {self.data["name"]}')
        xdotool.key(window_id, ['KP_Enter'])

    @QtCore.Slot()
    def on_trade_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/tradewith {self.data["name"]}')
        xdotool.key(window_id, ['KP_Enter'])

    @QtCore.Slot()
    def on_kick_from_party_clicked(self):
        window_id = xdotool.search(WINDOW_TITLE_REGEX_PATTERN)
        xdotool.windowactivate(window_id)
        xdotool.key(window_id, ['KP_Enter'])
        xdotool.type_(window_id, f'/kick {self.data["name"]}')
        xdotool.key(window_id, ['KP_Enter'])

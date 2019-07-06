from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QWidget

from pathofexile import client
from tradecompanion.views.tradewidget import Ui_TradeWidget


class TradeWidget(QWidget):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.ui = Ui_TradeWidget()
        self.ui.setupUi(self)

        self.data = data
        self.ui.buyer.setText(data['buyer'])
        self.ui.item.setText(data['item'])
        self.ui.price.setText(data['price'])
        self.ui.stash.setText(f'{data["league"]} ({data["stash"]} ({data["left"]}/{data["top"]}))')
        self.ui.other.setText(data['other'])
        self.ui.time.setText(self.data['time'].strftime('%H:%M:%S'))

    @QtCore.Slot()
    def on_copy_clicked(self):
        QApplication.clipboard().setText(self.data['item'])

    @QtCore.Slot()
    def on_whisper_clicked(self):
        window_id = client.find_path_of_exile_window()
        client.type_chat_message(window_id, f'@{self.data["buyer"]} ', submit=False)

    @QtCore.Slot()
    def on_invite_clicked(self):
        window_id = client.find_path_of_exile_window()
        client.type_chat_message(window_id, f'/invite {self.data["buyer"]}')

    @QtCore.Slot()
    def on_trade_clicked(self):
        window_id = client.find_path_of_exile_window()
        client.type_chat_message(window_id, f'/tradewith {self.data["buyer"]}')

    @QtCore.Slot()
    def on_kick_clicked(self):
        window_id = client.find_path_of_exile_window()
        client.type_chat_message(window_id, f'/kick {self.data["buyer"]}')

    @QtCore.Slot()
    def on_thanks_clicked(self):
        window_id = client.find_path_of_exile_window()
        client.type_chat_message(window_id, f'@{self.data["buyer"]} Thanks!')
        client.type_chat_message(window_id, f'/kick {self.data["buyer"]}')

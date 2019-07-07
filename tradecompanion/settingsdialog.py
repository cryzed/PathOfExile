from PySide2.QtWidgets import QDialog

from tradecompanion.views.settingsdialog import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

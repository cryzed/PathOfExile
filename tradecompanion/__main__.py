import argparse

from PySide2.QtWidgets import QApplication

from tradecompanion.mainwindow import MainWindow

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('path')


def main(arguments):
    application = QApplication()
    window = MainWindow(arguments.path)
    window.show()
    application.exec_()


if __name__ == '__main__':
    arguments = argument_parser.parse_args()
    argument_parser.exit(main(arguments))

import sys
import PyQt5
import logic
from functools import partial
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

buttons = {}


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Minesweeper"
        self.left = 10
        self.top = 10
        self.width = 480
        self.height = 640
        self.initUI()

    def setButtons(self):
        for y in range(16):
            for x in range(12):
                name = logic.minefield[y][x]
                buttons[(x, y)] = QPushButton(f" ", self)
                buttons[(x, y)].setGeometry(40, 40, 40, 40)
                buttons[(x, y)].move(x * 40, y * 40)
                buttons[(x, y)].clicked.connect(
                    partial(self.on_click, (x, y), buttons[(x, y)])
                )

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setButtons()
        self.show()

    def on_click(self, i, button):
        logic.step(i, button)
        button.setEnabled(False)

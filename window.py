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
        # y = 0
        # for i in range(12 * 16):
        #     if i == 12:
        #         y = 1
        #     x = i % 12
        #     if i % 12 == 0 and i > 13:
        #         y += 1
        #     name = logic.minefield[y][x]
        #     name = f"({x},{y})"
        #     self.button = QPushButton(f"{name}", self)
        #     self.button.setGeometry(40, 40, 40, 40)
        #     self.button.move((i % 12) * 40, y * 40)
        #     self.button.clicked.connect(partial(self.on_click, (i % 12, y), self.button.hide))
        for y in range(16):
            for x in range(12):
                name = logic.minefield[y][x]
                buttons[(x, y)] = QPushButton(f'{name}', self)
                buttons[(x, y)].setGeometry(40, 40, 40, 40)
                buttons[(x,y)].move(x * 40, y * 40)
                buttons[(x, y)].clicked.connect(partial(self.on_click, (x, y), buttons[(x, y)].hide))

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setButtons()
        self.show()

    def on_click(self, i, hide):
        logic.step(i, hide)
        hide()

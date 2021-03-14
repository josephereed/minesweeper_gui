import window
import sys
import random

minefield = [
    ['B' if random.randint(0, 7) == 1 else ' ' for col in range(0, 12)]
    for row in range(0, 16)
]

def search(x_y):
    sum = 0
    x, y = x_y
    for i in range(8):
        x_positions = [11, 11, 11, 0, 13, 13, 13, 0]
        y_positions = [15, 0, 17, 17, 17, 0, 15, 15] 
        new_x = (x + x_positions[i]) % 12
        new_y = (y + y_positions[i]) % 16
        if minefield[new_y][new_x] == 'B':
            sum += 1
    print(sum)


def step(x_y, hide):
    x, y = x_y
    if minefield[y][x] == 'B':
        value = minefield[y][x]
        print("BOOM GAME OVER", f"({x}, {y}) minefield[y][x] = {value}")
    else:
        hide()
        search(x_y)
        print("safe", f"({x}, {y})")


if __name__ == "__main__":
    app = window.QApplication(sys.argv)
    ex = window.App()
    sys.exit(app.exec())

from PySide2.QtGui import QGuiApplication, QWindow, QIcon, QImage, QPainter, QBackingStore  # type: ignore
# from PySide2.QtWidgets import QVBoxLayout # type: ignore
import sys
from typing import List


class Window(QWindow):
    def __init__(self, height: int, width: int, title: str, visible: bool = True) -> None:
        """Creates and configures Qt window
        """
        super(Window, self).__init__()
        self.setGeometry(50, 50, height, width)
        self.setTitle(title)

class ComponentFactory:
    def createQuitBtn(self):
        return


def main(args: List) -> None:
    """
    Arguments:
        args {List} -- sys.argv
    """
    app: QGuiApplication = QGuiApplication(args)
    window: Window = Window(600, 800, "Journal manager")
    window.setIcon(QIcon(str("./pyqt/fish.png")))
    width: int = 600
    height: int = 800
    frame: QImage = QImage(width, height, QImage.Format_RGB32)
    for x in range(width):
        for y in range(height):
            frame.setPixel(x, y, 0xffff00ff)
    qbs: QBackingStore = QBackingStore(window)
    window.show()
    sys.exit(app.exec_())
    return


if __name__ == "__main__":
    main(sys.argv)

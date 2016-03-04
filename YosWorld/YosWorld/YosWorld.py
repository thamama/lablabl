import sys
from PySide.QtCore import *
from PySide.QtGui import*
class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")

        self.mario=QImage("images/mario.png")

        self.rabbit=QImage("images/rabbit.png")
        self.pikachu = QImage("images/Singing_Pikachu_BW.png")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawImage(QRect(100,100,320,320),self.rabbit)
        p.drawImage(QRect(200,200,320,320),self.mario)
        p.drawImage(QRect(300,300,320,320),self.pikachu)
        p.end()


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())
   
        

import sys
from PySide.QtCore import *    
from PySide.QtGui import *   
class DrawWindow(QWidget):
     def __init__(self):
        QWidget.__init__(self,None)
        self.layout  = QHBoxLayout(self)
        

     def mousePressEvent(self, QMouseEvent):
        p = QPainter()
        p.begin(self)
        p.setPen(QColor(255,127,0))
        p.drawPoint(QMouseEvent.pos())
        p.end(self)
def main():
    
    app = QApplication(sys.argv)
    w = DrawWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
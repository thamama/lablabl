import sys
from PySide.QtCore import *    
from PySide.QtGui import *   
class DrawWindow(QWidget):
     def __init__(self):
        QWidget.__init__(self,None)
                
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
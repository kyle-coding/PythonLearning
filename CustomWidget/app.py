from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar import PowerBar

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    volume = PowerBar()
    volume.show()
    app.exec_()

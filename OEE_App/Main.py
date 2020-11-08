import sys
from OEE_App import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import pandas as pd
import OEE_DataProcessing as dp
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
matplotlib.use('QT5Agg')


PYCHARM_DEBUG = True


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def addmpl(self):
        # Adds the matplotlib graph to our "Graph" Tab
        fig1 = Figure()
        ax1f1 = fig1.add_subplot()
        ax1f1.plot(np.random.rand(5))

        # Add the plot:
        self.canvas = FigureCanvas(fig1)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()

        # Add the toolbar:
        self.toolbar = NavigationToolbar(self.canvas, self.graphWidget, coordinates=True)
        self.mplvl.addWidget(self.toolbar)

    def add_data_to_table(self):
        # Use our custom "PandasModel" class to set the model:
        self.tableView.setModel(PandasModel(OEE.df))
        self.tableView.setColumnWidth(0, 150)  # Timestamp column
        self.tableView.setColumnWidth(3, 120)  # OEE state column
        self.tableView.setColumnWidth(4, 200)  # Comment column

    # Create the main window from our "OEE_App.ui" file
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.canvas = 0  # This will be overwritten to be a FigureCanvas later

        # create the graph on our "Graph" tab:
        self.addmpl()

        # populate the data on our "Data" tab:
        self.add_data_to_table()


class PandasModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == "__main__":
    # Call our OEE processing class and get the data
    OEE = dp.OEEData()
    # OEE.calculate_accumulated_time()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

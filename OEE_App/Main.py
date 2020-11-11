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
from analoggaugewidget import AnalogGaugeWidget
from PyQt5.QtCore import Qt
import pyqtgraph

plt.style.use('fivethirtyeight')
matplotlib.use('QT5Agg')

PYCHARM_DEBUG = True


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def addmpl(self):
        # Adds the matplotlib graph to our "Graph" Tab
        fig1 = Figure()
        ax1f1 = fig1.add_subplot()
        ax1f1.plot(OEE.data_totalAvailable['Day of the Year'], OEE.data_totalAvailable['Total Time'])
        ax1f1.set_title('Available Time')
        ax1f1.set_xlabel('Day of the Year')
        ax1f1.set_ylabel('Time Available (min)')
        ax1f1.axis([300, 320, 0, 24])

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

    def modify_gauge(self, gauge, layout):
        gauge.enable_barGraph = True
        gauge.value_needle_snapzone = 1
        gauge.set_MaxValue(100)
        gauge.set_gauge_color_outer_radius_factor(1000)
        gauge.set_gauge_color_inner_radius_factor(600)
        gauge.value_min = 0
        gauge.update_value(30)
        gauge.scala_main_count = 1
        gauge.scala_subdiv_count = 1
        gauge.enable_scale_text = False
        gauge.enable_big_scaled_marker = False
        gauge.set_scale_polygon_colors([[.00, Qt.darkGreen],
                                        [.3, Qt.yellow],
                                        [0.8, Qt.red]])
        gauge.enable_CenterPoint = True
        layout.addWidget(gauge)

    def set_up_gauges(self):
        self.gauge1 = AnalogGaugeWidget()
        self.gauge2 = AnalogGaugeWidget()
        self.gauge3 = AnalogGaugeWidget()
        self.gauge4 = AnalogGaugeWidget()

        self.modify_gauge(self.gauge1, self.layout_gauge1)
        self.modify_gauge(self.gauge2, self.layout_gauge2)
        self.modify_gauge(self.gauge3, self.layout_gauge3)
        self.modify_gauge(self.gauge4, self.layout_gauge4)

    def plot_qt_graph(self):
        self.graph_qt_widget.setBackground('w')
        self.graph_qt_widget.setTitle("Availability", color='k', size='20pt')
        styles = {'color': 'k', 'font-size': '15px'}
        self.graph_qt_widget.setLabel('left', 'Available Time', **styles)
        self.graph_qt_widget.setLabel('bottom', 'Day of the Year', **styles)
        self.graph_qt_widget.addLegend(offset=(700,50))

        x = OEE.data_totalAvailable['Day of the Year']
        y = OEE.data_totalAvailable['Total Time']

        pen = pg.mkPen(color=(255, 0, 0), width=3, style=QtCore.Qt.SolidLine)
        self.line_available = self.graph_qt_widget.plot(x, y, pen=pen, name="Availability")

    def refresh_qt_graph(self):
        x = OEE.data_totalAvailable['Day of the Year']
        y = OEE.data_totalAvailable['Total Time']
        self.line_available.setData(x,y)

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.canvas = 0  # This will be overwritten to be a FigureCanvas later

        # create the graph on our "Graph" tab:
        self.addmpl()

        # populate the data on our "Data" tab:
        self.add_data_to_table()

        self.set_up_gauges()

        self.plot_qt_graph()



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

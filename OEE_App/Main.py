import sys
from OEE_App import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import pandas as pd
import OEE_DataProcessing as dp


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Set up our dataframe data:
        self.tableView.setModel(PandasModel(OEE.df))
        self.tableView.setColumnWidth(0, 150)  # Timestamp column
        self.tableView.setColumnWidth(3, 120)  # OEE state column
        self.tableView.setColumnWidth(4, 200)  # Comment column


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
    OEE.get_data()
    OEE.display_raw_data()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


from PyQt5 import QtSql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

from login import Ui_MainWindow as A_Ui # a界面的库
from main import Ui_MainWindow as B_Ui # b界面的库

from PyQt5 import QtCore, QtWidgets, QtSql
import sys

class AUi(QtWidgets.QMainWindow, A_Ui):
    def __init__(self):
        super(AUi, self).__init__()
        self.setupUi(self)

class BUi(QtWidgets.QMainWindow, B_Ui):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./1.db')
    model = QSqlTableModel()
    def __init__(self):
        super(BUi, self).__init__()
        self.setupUi(self)

    def view_data(self):


        self.model.setTable('product')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        delrow = -1

    def addrow(self):
        ret = self.model.insertRows(self.model.rowCount(), 1)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = AUi()
    a.show()
    b = BUi()
    # button是你定义的按钮
    a.pushButton.clicked.connect(
    	lambda:{a.close(), b.show(),b.view_data()}
   	)
    b.pushButton_3.clicked.connect(
        lambda:{b.addrow()}
    )

    sys.exit(app.exec_())



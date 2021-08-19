import sys
from PyQt5 import QtSql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


def initializeModel(model):
    model.setTable('product')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, 'pno')
    model.setHeaderData(1, Qt.Horizontal, 'pname')
    model.setHeaderData(2, Qt.Horizontal, 'pstandard')
def createView(title,model):
    view=QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view
def findrow(i):
    delrow=i.row()
    print('del row=%s' % str(delrow))

def addrow():
    ret=model.insertRows(model.rowCount(),1)
    print("insertRow=%s" % str(ret))
if __name__ == '__main__':
    app=QApplication(sys.argv)
    db=QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./1.db')
    model=QSqlTableModel()
    delrow=-1
    initializeModel(model)
    view=createView("展示数据",model)
    view.clicked.connect(findrow)

    dlg=QDialog()
    layout=QVBoxLayout()
    layout.addWidget(view)
    addBtn=QPushButton('添加一行')
    addBtn.clicked.connect(addrow)

    delBtn=QPushButton("删除一行")
    delBtn.clicked.connect(lambda :model.removeRow(view.currentIndex().row()))
    layout.addWidget(view)
    layout.addWidget(addBtn)
    layout.addWidget(delBtn)
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database demo")
    dlg.resize(500,400)
    dlg.show()
    sys.exit(app.exec_())

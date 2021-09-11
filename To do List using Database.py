from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

con = sqlite3.connect("list.db")

cur = con.cursor()

cur.execute("Create Table if not exists ToDoList(list_items text)")

con.commit()
con.close()

class Ui_MainWindow(object):
    l = []
    file_name = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(0, 140, 531, 451))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.b1 = QtWidgets.QPushButton(self.centralwidget, clicked = self.add_item)
        self.b1.setGeometry(QtCore.QRect(30, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget, clicked = self.delete_item)
        self.b2.setGeometry(QtCore.QRect(200, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget, clicked = self.clear_list)
        self.b3.setGeometry(QtCore.QRect(380, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.e1 = QtWidgets.QLineEdit(self.centralwidget)
        self.e1.setGeometry(QtCore.QRect(10, 10, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.e1.setFont(font)
        self.e1.setObjectName("e1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())

        self.actionSave.triggered.connect(self.save)
        self.actionAbout.triggered.connect(self.about)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open()

    def about(self):
        QtWidgets.QMessageBox.about(self.centralwidget, "About", "This To Do List is Made by Jwalant Modi")

    def open(self):
        con = sqlite3.connect("list.db")

        cur = con.cursor()

        records = cur.execute("Select * from ToDoList")

        for record in records:
            self.listWidget.addItem(str(record[0]))

        con.commit()
        con.close()
        self.listWidget.setCurrentIndex(QtCore.QModelIndex())

    def save(self):
        items = []

        for i in range(self.listWidget.count()):
            items.append(self.listWidget.item(i).text())

        con = sqlite3.connect("list.db")

        cur = con.cursor()

        cur.execute("Delete from ToDoList")

        for item in items:
            cur.execute("Insert into ToDoList values('"+item+"')")
   
        con.commit()
        con.close()
  
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("Save")
        message.setText("Data is Succesfully Stored in Database")
        message.setIcon(QtWidgets.QMessageBox.Information)
        message.exec_()

    def add_item(self):
        t1 = self.e1.text()
        if t1 != "":
            self.listWidget.addItem(t1)
            self.e1.setText("")

    def delete_item(self):
        try:
            i = self.listWidget.currentRow() # returns index of selected item
            print(i)
            if i!=-1:
                self.listWidget.takeItem(i)
                self.listWidget.setCurrentRow(-1)
            
        except Exception as e:
            pass

    def clear_list(self):
        self.listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To do List"))
        self.listWidget.setSortingEnabled(True)
        self.b1.setText(_translate("MainWindow", "Add Item"))
        self.b2.setText(_translate("MainWindow", "Delete Item"))
        self.b3.setText(_translate("MainWindow", "Clear List"))
        self.e1.setPlaceholderText(_translate("MainWindow", "Type Here"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

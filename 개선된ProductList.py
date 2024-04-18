import sys
import os.path
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import uic

# 데이터베이스 관리 클래스
class DatabaseManager:
    def __init__(self, db_name="ProductList.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.initialize_database()

    def initialize_database(self):
        if not os.path.exists(self.db_name):
            self.cursor.execute("create table Products (id integer primary key autoincrement, Name text, Price integer);")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.DatabaseError as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Exception in query: {e}")

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        self.connection.close()

# 메인 윈도우 클래스
class Window(QMainWindow, uic.loadUiType("ProductList3.ui")[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database_manager = DatabaseManager()
        self.initialize_ui()

    def initialize_ui(self):
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)
        self.getProduct()

    def addProduct(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.database_manager.execute_query("insert into Products (Name, Price) values(?,?);", (name, price))
        self.getProduct()

    def updateProduct(self):
        product_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.database_manager.execute_query("update Products set name=?, price=? where id=?;", (name, price, product_id))
        self.getProduct()

    def removeProduct(self):
        product_id = self.prodID.text()
        self.database_manager.execute_query("delete from Products where id=?;", (product_id,))
        self.getProduct()

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.database_manager.fetch_all("select * from Products;")
        for row_index, item in enumerate(products):
            self.tableWidget.setItem(row_index, 0, QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(row_index, 1, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(row_index, 2, QTableWidgetItem(str(item[2])))

    def doubleClick(self):
        row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(row, 0).text())
        self.prodName.setText(self.tableWidget.item(row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    sys.exit(app.exec_())

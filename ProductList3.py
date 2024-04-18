# 필요한 라이브러리를 임포트합니다.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# 데이터베이스 연결
if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else: 
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    # 테이블이 존재하지 않는 경우 테이블 생성
    cur.execute(
        "create table Products (id integer primary key autoincrement, Name text, Price integer);")

# UI 파일 로드
form_class = uic.loadUiType("ProductList3.ui")[0]

# 메인 윈도우 클래스 정의
class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 초기화
        self.id = 0 
        self.name = ""
        self.price = 0 

        # 테이블 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 엔터 키로 다음 입력 필드로 이동
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 테이블 더블 클릭 이벤트 연결
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    # 제품 추가 함수
    def addProduct(self):
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("insert into Products (Name, Price) values(?,?);", 
            (self.name, self.price))
        self.getProduct() 
        con.commit() 

    # 제품 업데이트 함수
    def updateProduct(self):
        self.id  = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("update Products set name=?, price=? where id=?;", 
            (self.name, self.price, self.id))
        self.getProduct() 
        con.commit()  

    # 제품 삭제 함수
    def removeProduct(self):
        self.id  = self.prodID.text() 
        strSQL = "delete from Products where id=" + str(self.id)
        cur.execute(strSQL)
        self.getProduct() 
        con.commit()  

    # 제품 목록 가져오는 함수
    def getProduct(self):
        # 테이블 내용을 지우고
        self.tableWidget.clearContents()
        # 제품 목록을 가져와서 테이블에 출력
        cur.execute("select * from Products;") 
        row = 0 
        for item in cur: 
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 0, itemID)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 2, itemPrice)
            row += 1
            print("row: ", row)  

    # 테이블 더블 클릭 시 해당 제품 정보 입력 필드에 표시
    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

# 애플리케이션 실행
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()

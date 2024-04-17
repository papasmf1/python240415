# BankAccount.py
import 상속01 as c1 
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #멤버변수를 초기화(이름 숨김)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        #입금 
        self.__balance += amount 
    def withdraw(self, amount):
        #출금
        self.__balance -= amount
    def __str__(self):
        #현재 상태를 문자열로 출력 
        return "{0} , {1} , {2}".format(self.__id, 
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)

demo = c1.Person("박문수", "010-222") 
demo.printInfo()
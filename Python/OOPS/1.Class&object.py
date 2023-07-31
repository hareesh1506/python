# CONSTRUCTER
"""
class Constractor:
    def __init__(self):
        print('this method is called only when class called')
o1 = Constractor()
"""
# BANKACCOUNT
"""
class BankAccount:
    def __init__(self,acc_no,acc_name,ifsc,bals):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.ifsc = ifsc
        self.bals = bals
    def Display(self):
        print("details are::",self.acc_no,self.acc_name,self.ifsc,self.bals)
obj1 = BankAccount(1234561234,'hari','ANDB000339',1000000)
obj1.Display()
"""

# prac1
"""
class BankAccount:
    def __init__(self,acc_name,acc_no,acc_ifsc,acc_blz):
        self.acc_name = acc_name
        self.acc_no = acc_no
        self.acc_ifsc = acc_ifsc
        self.acc_blz = acc_blz
    def withdraw(self,amount):
        self.acc_blz-= amount
    def deposit(self,amount):
        self.acc_blz += amount
    def check_blz(self):
        print(self.acc_blz)

obj1 = BankAccount('hareesh',987654321,'aszdxfcgv',250000)
obj1.check_blz()
# deposite money
obj1.deposit(2000)
# check blz
obj1.check_blz()
# withdraw
obj1.withdraw(250000)
# checkblz
obj1.check_blz()
"""


# MOBILES
"""
"""
class Mobiles:
    def __init__(self,name,cost,ram,storage):
        self.name = name
        self.cost = cost
        self.ram = ram
        self.storage = storage

    def oneplus_mobiles(self):
        print(self.name,self.cost,self.ram,self.storage)
    def iphone_mobiles(self):
        print(self.name,self.cost,self.ram,self.storage)



obj1=Mobiles('1+nordce2',25000,'12gb',128)
obj2=Mobiles('iphone-X',50000,'12gb',128)
obj1.oneplus_mobiles()
obj2.iphone_mobiles()
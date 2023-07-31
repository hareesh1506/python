# A SINGLE CLASS CAN CREATE BY MORETHEN ONE PARENT CLASS

class Father:
    def method1(self):
        print('i am father')
class mother:
    def method2(self):
        print('i am mother')
class child(Father,mother):
    def method3(self):
        print('i am child')

object1 = child()
object1.method3()
object1.method2()
object1.method1()


class Father:
    def m1(self):
        print('father')
class Mother:
    def m2(self):
        print('father')
class child(Father,Mother):
    def m3(self):
        print('child')

# oj1 = child()
# oj1.m3()
# oj1.m2()
# oj1.m1()


oj1 = Mother()
oj1.m3()
oj1.m2()
oj1.m1()



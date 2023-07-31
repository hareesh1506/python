"""
class dad:
    def method1(self):
        print('im dad')

class child(dad):
    def method2(self):
        print('im child')
# {right way}
# obj1 = child()
# obj1.method2()#we can access
# obj1.method1()#we can access

# {wrong way}
# obj2 = dad()
# obj2.method1()
# obj2.method2()

"""

# SINGLE INHERITENCE-- A PARENT CAN ACCESS PARENT FEATURES BUT PARENT CAN NOT ACCESS CHILD FEATURES

class parent:
    def feature1(self):
        print('i am parent class')
class child(parent):
    def feature2(self):
        print('i am child class')
object1 = child()
object1.feature1()
object1.feature2()
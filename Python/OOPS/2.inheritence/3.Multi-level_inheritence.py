# MULTI-LEVEL INHERITENCE -- WITH THE HELP OF ONE PARENT CREATE A CHILD WITH THE HELP OF CHILD THEN AGAIN CREATE A CHILD
# GRAND-PARENT>>>PARENT>>>CHILD
"""
class ABC:
    def m1(self):
        print('grand parent')
class AB(ABC):
    def m2(self):
        print('parent')
class A(AB):
    def m3(self):
        print('child')
pet = A()
# pet.m3()
# pet.m2()
# pet.m1()
"""


class grandparent:
    def m1(self):
        print('grand parent')
class parent(grandparent):
    def m1(self):
        print('parent')
class child(parent):
    def m3(self):
        print('child')

cl = child()
cl.m1()
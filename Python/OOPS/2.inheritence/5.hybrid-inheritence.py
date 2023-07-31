class grandparent:
    def method1(self):
        print('I AM GRAND PARENT')
class parent1(grandparent):
    def method2(self):
        print('I AM PARENT1')
class parent2:
    def method3(self):
        print('I AM PARENT2')
class child(parent1,parent2):
    def method4(self):
        print('I AM CHILD')

# obj=child()
# obj.method1()
# obj.method2()
# obj.method3()
# obj.method4()


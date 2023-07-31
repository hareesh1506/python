class parent:
    def m1(self):
        print('parent')
class child1(parent):
    def m2(self):
        print('child_1')
class child2(parent):
    def m3(self):
        print('child2')

print('child1 class ::')
vot = child1()
vot.m1()
vot.m2()
print('child2 class ::')
vot = child2()
vot.m3()
vot.m1()




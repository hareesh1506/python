import unittest

def sum(a,b):
    return a + b
class sumtest(unittest.TestCase):
    def setUp(self):
        print('SETUP CALLED...')
        self.a =10
        self.b =20
    def tearDown(self):
        self.a = 0
        self.b = 0
        print('TEARDOWN STARTED...')
    def tets_sumfunc1(self):
        print('TEST-1 CALLED...')

        #Act
        result = sum(self.a,self.b)
        #Assert
        self.assertEqual(result, self.a+self.b)
    def tets_sumfunc2(self):
        print('TEST-2 CALLED...')

        #Act
        result = sum(self.b,self.a)
        #Assert
        self.assertEqual(result, self.a+self.b)
if __name__ == "__main__":
    unittest.main()
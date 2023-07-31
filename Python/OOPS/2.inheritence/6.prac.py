"""
# class faculity:
#     def __init__(self,firstname,lastname,email,faculityid,address,mobileno,subjectsTeaching,salary,datejoining):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email
#         self.faculityid = faculityid
#         self.address = address
#         self.mobileno = mobileno
#         self.subjectsTeaching = subjectsTeaching
#         self.salary = salary
#         self.datejoining = datejoining
#     def getfullname(self):
#         print(self.firstname,"",self.lastname)
#     def changeaddress(self,newaddress):
#         self.address=newaddress
#         print("address changed")
#     def changenumber(self,newnumber):
#         self.mobileno=newnumber
#         print('number updated done')
#     def getsalary(self):
#         print('you have sal::', self.salary)
#
# obj1 = faculity('hari','chowdary','hare01@',2013001,'ktc',7993,7,30000,'june15')
# obj1.getfullname()
#
#
#
#
#
#
# # obj1=faculity('hareesh','chowdary','hareeshitl02@',2012341,'kothacheruvu',7993,6,30000)
# # obj1.getfullname()
#
# class Student:
#     def __init__(self, firstname, lastname, email, Studentid, address, mobileno, subjectsLearned, GPA,datejoining):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email
#         self.Studentid = Studentid
#         self.address = address
#         self.mobileno = mobileno
#         self.subjectsLearned = subjectsLearned
#         self.GPA = GPA
#         self.datejoining = datejoining
#
#     def getfullname(self):
#         print(self.firstname, " ", self.lastname)
#
#     def changeaddress(self, newaddress):
#         self.address = newaddress
#         print("address changed")
#
#     def changenumber(self, newnumber):
#         self.mobileno = newnumber
#         print('number updated done')
#
#     def getGPA(self):
#         print('you have sal::', self.GPA)

"""

# seperate all common attributes and methods from both faculity and student classes
class Member:
    def __init__(self,firstname,lastname,email,memberid,address,mobileno,datejoining):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.memberid = memberid
        self.address = address
        self.mobileno = mobileno
        self.datejoining = datejoining
    def getfullname(self):
        print(self.firstname, " ", self.lastname)

    def changeaddress(self, newaddress):
        self.address = newaddress
        print("address changed")

    def changenumber(self, newnumber):
        self.mobileno = newnumber
        print('number updated done')
class faculity(Member):
    def __init__(self,firstname,lastname,email,memberid,address,mobileno,subjectsTeaching,salary,datejoining):
        self.subjectsTeaching = subjectsTeaching
        self.salary = salary
        Member.__init__(self,firstname,lastname,email,memberid,address,mobileno,datejoining)
    def getsalary(self):
        print(self.salary)

class student(Member):
    def __init__(self,firstname, lastname, email, memberid, address, mobileno, subjectsLearned, GPA,datejoining):
        self.subjectsLearned = subjectsLearned
        self.GPA = GPA
        Member.__init__(self,firstname,lastname,email,memberid,address,mobileno,datejoining)
    def getGPA(self):
        print(self.GPA)







# class ComplexNumber:
#     def __init__(self,real = 0,imaginary = 0):
#         self.real = real
#         self.imag = imaginary
    
#     def getData(self):
#         print("{0}+{1}j".format(self.real,self.imag))

# num = ComplexNumber(2,3)
# num.getData()

class Student:
    def __init__(self,name,age,mobile,token):
        self.name = name
        self.age = age
        self.mobile = mobile
        self.token = token
    def getData(self):
        self.name = input("Enter name:")
        self.age = input("Enter age:")
        self.mobile = input("Enter mobile:")
        self.token = input("Enter token:")
    def display(self):
        print("I am {0}, i am {1} years old. \nMy token number is {3}, and you can reach me at {2}".format(self.name,self.age,self.mobile,self.token))

student1 = Student("Vivek",20,9876543210,2034)
student1.getData()
student1.display()
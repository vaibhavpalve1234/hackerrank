# class cricket :
#     def __init__(self,name,runs):
#         self.player_name=name
#         self.runs=runs
    
#     def avg(self):
#         print("Plyer name",self.player_name)
#         print("runs :",self.runs)


# c=cricket("dhoni",18000)
# c1=cricket("rohit",21000)
# c.avg()
# c1.avg()




# class computer :
#     def __init__(self):
#         self.name="vaibhav"
#         self.age=50

#     def compare(self,c1):
#         if self.age==c1.age:
#             return True
#         else :
#             return False
# c=computer()
# c1=computer()
# c1.age=5

# if c.compare(c1):
#     print("they same age")
# else :
#     print("they are difference")

# class s  :
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def compare(self,c1):
#         if c.age==c1.age:
#             return True
#         else :
#             return False

# c=s ("vaibhav",21)
# c1=s("pratiksha",19)
# if c.compare(c1):
#     print("same age ",)
# else :
#     print(" mot same age")


# class car :
#     wheel = 4 
    


#     def __init__(self):
#         self.name="BMW"
#         self.mil=10
# car.wheel=5
# c = car()
# print(c.name,c.wheel)
# print(c.mil)

# class student :
#     school ="rait"
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         summ=(self.m1+self.m2+self.m3)/3
#         return  summ
#     @classmethod
#     def getschool(cls):
#         return cls.school
#     @staticmethod
#     def info():
#         print("this a student name ")

# print(student.getschool())
# c=student(33,25,89)
# c1=student(75,78,78)
# print(c.avg())
# print(c1.avg())
# print(student.info())

# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.laptop()
    
#     def show(self):
#         print(self.name,self.rollno)

#     class laptop :
#         def __init__(self):
#             self.brand="hp"
#             self.cpu="i5"
#             self.ram=85
#         def show (self):
#             print(self.brand,self.cpu,self.ram)



# s1=student("vaibhav",36)
# s2=student("ketan",97)
# s1.show()
# s2.show()
# l1=student.laptop()
# print(l1.show())

# class a:
#     def feature1(self):
#         print("feature 1 working")
#     def feature2(self):
#         print("feature 2 working")
# class b(a):
#     def feature3(self):
#         print("feature 3 working")
#     def feature4(self):
#         print("feature 4 working")
# class c(b):
#     def feature5(self):
#         print("feature 1 working")
#     def feature6(self):
#         print("feature 2 working")

# a1=a()
# a1.feature1()
# a1.feature2()
# b4=b
# b.feature1()
# c1=c

print(int.__add__(7,8))
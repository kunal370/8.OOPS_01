
class Student: # class
    #default constructor
    def __int__(self):
        pass

    #parameterized constructor
    def __init__(self,stu_name,stu_marks,stu_age): #constructor
        self.name=stu_name
        self.marks=stu_marks
        self.age=stu_age
        print("adding new student...")

s1=Student("karan",78,23) # object
print(s1.name,s1.marks,s1.age)

s2=Student("arjun",67,21)
print(s2.name,s2.marks,s2.age)


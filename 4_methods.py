# creating class
class Student:
    def __init__(self,stu_name,stu_marks):
        self.name=stu_name
        self.marks=stu_marks

    #defining method
    def get_name(self):
        print("hello students",s1.name)
    def  get_marks(self):
        print("marks are: ",s1.marks)

# creating object
s1=Student("sonu",89)
print(s1.name,s1.marks)
s1.get_name()
s1.get_marks()




class Student:
    def __init__(self,stu_name,sub1,sub2,sub3):
        self.name=stu_name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def avg_marks(self):  # this is normal method
        avg=(s1.sub1+s1.sub2+s1.sub3)/3
        print("hi",s1.name,"your avg score is:",avg)

    @staticmethod   #decorator
    def hello():   # this is static method
        print("hello")


s1=Student("sonu",89,78,82)
print(s1.name,s1.sub1,s1.sub2,s1.sub3)
s1.avg_marks()

s1.hello()
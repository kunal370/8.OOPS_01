#create a student class that takes name, marks of 3 subjects as arguments in constructor.
#then create a method to print the average

class Student:
    def __init__(self,stu_name,sub1,sub2,sub3):
        self.name=stu_name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def avg_marks(self):
        avg=(s1.sub1+s1.sub2+s1.sub3)/3
        print("hi",s1.name,"your avg score is:",avg)


s1=Student("sonu",89,78,82)
print(s1.name,s1.sub1,s1.sub2,s1.sub3)
s1.avg_marks()

s1.name="kunal"  # can directly chnage the name os sub marks
s1.avg_marks()

s1.sub1=99
s1.avg_marks()
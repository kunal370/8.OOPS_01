
class Student: # class

    collage_name="RCERT" #class attribute
    name="anonymous"
    #parameterized constructor
    def __init__(self,stu_name,stu_marks): #constructor
        self.name=stu_name #object attribute
        self.marks=stu_marks
        print("adding new student...")

s1=Student("karan",78) # object
print(s1.name,s1.marks)

s2=Student("arjun",67)
print(s2.name,s2.marks)

print(s2.collage_name)

# class attribute < object attribute   <-- always
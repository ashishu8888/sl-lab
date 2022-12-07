class Student:

    def __init__(self):
        self.name = input("Enter name of student\n")
        self.age = input("Enter age of the student\n")
        self.marks = []

    def display(self):
        print(self.name,self.age,self.marks)

    def accept(self):
        a = input("Enter marks of subject 1: \n")
        b = input("Enter marks of subject 2: \n")
        c = input("Enter marks of subject 3: \n")

        self.marks.append(a)
        self.marks.append(b)
        self.marks.append(c)


student = Student()
student.accept()

student.display()

        

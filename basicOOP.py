class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrades: {self.grades}")

    def cal_average_grade(self):
        return sum(self.grades)/len(self.grades)

def input_grades():
    grades = input("Enter numbers separated by a comma: ")
    grades = grades.split(',')
    grades = [int(item.strip()) for item in grades]
    return grades

name = input(f"Enter name: ")
age = input(f"Enter age: ")
grades = input_grades()
student1 = Student(name, age, grades) 
student1.display_details()

average_grade =   student1.cal_average_grade()  
print(f"Avergae grade: {average_grade}")  


        
#create operation
def add_student(data, name, age, grades):
    if name in data:
        print(f"Student {name} already exists.")
    else:
        data[name] = {'age':age, 'grades':grades}
        print(f"Student {name} added successfully.")

#read operation
def get_student(data, name):
    if name in data:
        print(f"Details of {name}: {data[name]}")
    else:
        print(f"Student {name} not found")

#update operation
def update_student(data, name, age, grades):
    if name in data:
        data[name]['age'] = age
        data[name]['grades'] = grades
        print(f"Student {name} updated succesfully")
    else:
        print(f"Student {name} not found")

#delete operation
def delete_student(data, name):
    if name in data:
        del data[name]
        print(f"Student {name} deleted successfully")
    else:
        print(f"Student {name} not found")

#inputting grades
def input_grades():
    grades = input("Enter numbers separated by a comma: ")
    grades = grades.split(',')
    grades = [int(item.strip()) for item in grades]
    return grades

#dictionary data structures used for student
student = {}

while True:
    print(f"1]create\n2]read\n3]update\n4]delete\n5]exit\n")
    choice = input(f"choose: \t")

    if choice == '1':
        name = input(f"Enter name: ")
        age = input(f"Enter age: ")
        grades = input_grades()
        add_student(student,name,age,grades)

    elif choice == '2':
        name = input(f"Enter name: ")
        get_student(student,name)
    
    elif choice == '3':
        name = input(f"Enter name: ")
        age = input(f"Enter age: ")
        grades = input_grades()
        update_student(student,name,age,grades)

    elif choice == '4':
        name = input(f"Enter name: ")
        delete_student(student,name)
    elif choice == '5':
        print(f"exiting......")
    else: 
        print("Invalid choice. Please try again.")
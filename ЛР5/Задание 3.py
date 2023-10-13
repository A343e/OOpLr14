class Student:
    def __init__ (self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades
    def print_info(self):
        print(f"Студент: {self.name}")
        print(f"Номер группы: {self.group}")
        print(f"Успеваемость: {self.grades}")
students = []
for _ in range(10):
    name = input("Введите Ф.И. студента: ")
    group = input("Введите номер группы: ")
    grades = []
    for i in range(5):
        grade = float(input(f"Введите оценку за предмет {i+1}: "))
        grades.append(grade)
    student = Student(name, group, grades)
    students.append(student)
# Сортировка студентов по увелечению среднего балла
students.sort(key=lambda student: sum(student.grades) / len(student.grades))
# Вывод информации о студентах
for student in students:
    student.print_info()
    print()

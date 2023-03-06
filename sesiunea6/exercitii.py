# 1 sa se creeze o clasa student cu atributele numele, universitate, an (toate la constructor)
# 2 sa se creeze functile specifice astfel incat la printarea unui student se afiseaza toate atributele acestuia
# 3 fie lista de studenti
# a. sa se creeze clasa de studenti db in care sa se adauge ca si atribut de clasa lista de studenti
# b. sa se creeze o functie care primesteca parametru numele unui student si verifica dacastd este inregistrat la vreo univ
# c. sa se creeze o functie care adauga un student in lista
class Student:
    def __init__(self, name, university, year):
        self.name = name
        self.university = university
        self.year = year

    def __str__(self):
        return f"name : {self.name} university : {self.university} year : {self.year}"

    def __repr__(self):
        return str(self)

d = Student("Mike", "UMC", 2010)
print(d)

class StudentDB:
    students =  [
        Student(name="Alex", university="Babes", year=3),
        Student(name="Cristina", university="Yale", year=4),
        Student(name="Meredith", university="Chicago", year=3),
        Student(name="George", university="Harvard", year=1),
        Student(name="Mark", university="NYU", year=4),
        Student(name="Owen", university="NYU", year=4),
        Student(name="Derek", university="Columbia", year=4)
    ]
    def check_enroll_student(self, name):
        for student in self.students:
            if name == student.name and student.university:
                return True
        return False
    def add_student(self, student):
        self.students.append(student)



db = StudentDB()
print(db.check_enroll_student("Mark"))
db.add_student(Student("Mike", "UMC", 2010))
print(db.students)
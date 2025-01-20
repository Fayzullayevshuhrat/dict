

class Pupil:
    def __init__(self, name, yil, sinf):
        self.name = name
        self.yil = yil
        self.sinf = sinf

    def info(self):
        return f"Pupil Name: {self.name}, Year: {self.yil}, Class: {self.sinf}"


class Student:
    def __init__(self, name, yil, kurs, fakultet):
        self.name = name
        self.yil = yil
        self.kurs = kurs
        self.fakultet = fakultet

    def info(self):
        return f"Student Name: {self.name}, Year: {self.yil}, Course: {self.kurs}, Faculty: {self.fakultet}"


class PDPManagement:
    def __init__(self):
        self.students = {}
        self.pupils = {}

    def add_st(self, student_id, student):
        self.students[student_id] = student

    def add_pu(self, pupil_id, pupil):
        self.pupils[pupil_id] = pupil

    def remove_st(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def remove_pu(self, pupil_id):
        if pupil_id in self.pupils:
            del self.pupils[pupil_id]

    def info_st(self):
        return [student.info() for student in self.students.values()]

    def info_pu(self):
        return [pupil.info() for pupil in self.pupils.values()]


# Example usage:
pdp_management = PDPManagement()

# Adding pupils
pupil1 = Pupil(name="Bobur", yil=2025, sinf="5th")
pupil2 = Pupil(name="Aziz", yil=2025, sinf="6th")
pdp_management.add_pu(pupil_id=1, pupil=pupil1)
pdp_management.add_pu(pupil_id=2, pupil=pupil2)

# Adding students
student1 = Student(name="Aslbek", yil=2025, kurs="1st", fakultet="Computer Science")
student2 = Student(name="sherbek", yil=2025, kurs="2nd", fakultet="Mathematics")
pdp_management.add_st(student_id=1, student=student1)
pdp_management.add_st(student_id=2, student=student2)

# Printing information
print("Pupils Info:")
for info in pdp_management.info_pu():
    print(info)

print("\nStudents Info:")
for info in pdp_management.info_st():
    print(info)

# Removing a pupil and a student
pdp_management.remove_pu(1)
pdp_management.remove_st(2)

# Printing updated information
print("\nUpdated Pupils Info:")
for info in pdp_management.info_pu():
    print(info)

print("\nUpdated Students Info:")
for info in pdp_management.info_st():
    print(info)

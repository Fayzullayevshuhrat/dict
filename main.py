from problem2 import *

from problem2 import *

# Create some pupils and students
pupil1 = Pupil("Bobur", 2025, "5th")
pupil2 = Pupil("Aziz", 2025, "6th")

student1 = Student("Aslbek", 2025, "1st", "Computer Science")
student2 = Student("Sherbek", 2025, "2nd", "Mathematics")

# Create PDPManagement instance to manage students and pupils
pdp_management = PDPManagement()

# Add pupils and students to the management system
pdp_management.add_pu(1, pupil1)
pdp_management.add_pu(2, pupil2)
pdp_management.add_st(1, student1)
pdp_management.add_st(2, student2)

# Print information about students and pupils
print("Pupils Info:")
for info in pdp_management.info_pu():
    print(info)

print("\nStudents Info:")
for info in pdp_management.info_st():
    print(info)

# Remove a pupil and a student
pdp_management.remove_pu(1)
pdp_management.remove_st(2)

# Print updated information
print("\nUpdated Pupils Info:")
for info in pdp_management.info_pu():
    print(info)

print("\nUpdated Students Info:")
for info in pdp_management.info_st():
    print(info)

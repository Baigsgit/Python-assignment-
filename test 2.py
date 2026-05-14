# Student Result Management System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter data for Student {i+1}")

    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ").title()

    chemistry = int(input("Enter Chemistry Marks: "))
    physics = int(input("Enter Physics Marks: "))
    maths = int(input("Enter Maths Marks: "))

    total = chemistry + physics + maths
    percentage = (total / 300) * 100


    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    students.append([roll, name, chemistry, physics, maths,
                     total, percentage, grade])

print("\n" + "="*70)
print("STUDENT REPORT CARD")
print("="*70)

print(f"{'Roll':<8}{'Name':<15}{'Total':<10}{'Percentage':<15}{'Grade'}")

for student in students:
    print(f"{student[0]:<8}{student[1]:<15}{student[5]:<10}"
          f"{student[6]:<15.2f}{student[7]}")
    


    
# ## #######################   Quation 1
# method 1
# Students_Garade = [95, 50, 60, 80, 80, 73, 90]
# total = 0
# for student in Students_Garade:
#     print("The student grade is: ", student)
#     total = total+student
# print("The final total is: ", total)
# print(total/len(Students_Garade))

# method 2
Studen_grades = []
while True:
    Studen_grade = input("Enter a grade (or 'q' to quit): ")
    if len(Studen_grade) > 2:
        print("Please Enter only two Numbers")
    else:
        if Studen_grade.lower() == 'q':
            break
        Studen_grades.append(float(Studen_grade))
total = sum(Studen_grades)
average = total / len(Studen_grades)
print("The average Studen_grades is:", average)

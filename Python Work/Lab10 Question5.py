#Mary Kate Sheehan
#11/14/2023
#Lab10 Question5


try:
    grades_file = open("grades.txt", "r")
    for line in grades_file:
        grades = line.strip()
            
    total = len(grades)
    failing_grades = 0
    passing_grades = 0
    average_grade = sum(grades) / num_students
    highest_grade = max(grades)
    lowest_grade = min(grades)

    for grade in grades_file:    
        if grade > 59:
            passing_grades += 1

        elif grade <= 59:
            failing_grades += 1

except IOError as e:
    print("File not found!")

print("There are", total, "number of grades.")
print("The highest grade is", hightest_grade)
print("The lowest grade is", lowest_grade)
print("The average grade is", average_grade)
print("You have a total of", passing_grades, "passing grades")
print("You have a total of", failing_grades, "failing grades")











#Mary Kate Sheehan
#10/31/2023
#Lab 8 Question 4


def grade_average(test1,test2,test3,test4,test5):
    grade = (test1 + test2 + test3 + test4 + test5) / 5
    return grade

def letter_grade(grade):  
    if grade >= 90 and grade <= 100:
        return "A"
    
    elif grade >= 80 and grade <= 89:
        return "B"
    
    elif grade >= 70 and grade <= 79:
        return "C"
    
    elif grade >= 60 and grade <= 69:
        return "D"
    
    else:
        return "F"
    

def main():
    test1 = int(input("Enter first test grade: "))
    test2 = int(input("Enter second test grade: "))
    test3 = int(input("Enter third test grade: "))
    test4 = int(input("Enter fourth test grade: "))
    test5 = int(input("Enter fifth test grade: "))
    grade = grade_average(test1,test2,test3,test4,test5)

    print("Your average of these five tests is", grade_average(test1,test2,test3,test4,test5))
    print("Your average letter grade of these five tests is", letter_grade(grade))

main()

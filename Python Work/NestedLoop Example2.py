#Mary Kate Sheehan
#10/11/2023
#Find the average of n tests for n students

m = int(input("Enter the number of students in your classroom: "))
n = int(input("Enter the numbers of tests per student: "))

#Student loop is the outer loop
for students in range(m):
    test_sum = 0
    #Test loop is the inner loop
    #The rule says we do not go to the next loop in the outer loop until we complete all the loops of the inner loop
    for test in range(n):
        grade = eval(input("Enter the test score of the student: "))
        test_sum = test_sum + grade

    print("The average score of the student", students, "is", round(test_sum / num_tests, 2))

#How many repetitions in total do we have? m * n Defines the complexity of the algorithmn because you can have a very big number of repetitions
        

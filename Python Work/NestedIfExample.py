#Mary Kate Sheehan
#9/27/2023
#nested if example

score = eval(input("Enter a score: "))

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

print("This is the end of the program.")

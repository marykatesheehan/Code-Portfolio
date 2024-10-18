#Mary Kate Sheehan
#10/31/2023
#Lab 8 Question 5

def zeroCheck(num1,num2,num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return True
    else:
        return False
    

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    print("You entered a zero as one of your integers:", zeroCheck(num1,num2,num3))

main()

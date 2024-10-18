#Mary Kate Sheehan
#11/7/2023
#Lab 9 Question 2


def is_prime(num):
    for i in range(2 ,int(num//2) + 1):
        if num % i == 0:
            return False
    else:
        return True
    

def main():
    num = int(input("Enter an integer: "))
    print("The number is prime:", is_prime(num))
    
main()



    

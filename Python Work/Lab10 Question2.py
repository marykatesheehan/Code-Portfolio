#Mary Kate Sheehan
#11/14/2023
#Lab10 Question2

def fib(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        fprev1 = 1
        fprev2 = 0
        
        for i in range(2, n + 1):
            fprev2, fprev1 = fprev1, fprev2 + fprev1

        return fprev1
       

def main():
    n = int(input("Enter a number: "))

    if n < 0:
        n = int(input("Please enter a non-negative number: "))
    
    print(fib(n))

main()
    

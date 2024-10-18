#Mary Kate Sheehan
#11/14/2023
#Lab10 Question4

n = int(input("Enter a positie integer: "))
m = int(input("Enter a positie integer: "))

for i in range(1, n+1) :
        for j in range(1, m+1) :
            if i == 1 or i == n or j == 1 or j == m:
                print("@", end="")            
            else :
                print(" ", end="")            
         
        print()

#Mary Kate Sheehan
#10/16/2023
#Multiplication tables using nested loops

for i in range(11): #this is outer loop
    print("-------------------------")
    print("Multiplication tables of",i)
    for j in range(10): #this is inner loop
        print(i,"*",j,"=",i*j)
    print("-------------------------")


    
#outer loop i = 1
#loop iteration                        
    #inner loop
        #j = 1   
        #1 * 1 = 1                            
        #j = 2
        #1 * 2 = 2
        #j = 3
        #1 *1 = 3
        #.
        #.
        #.
        #j = 10
        #1 * 10 = 10

#Mary Kate Sheehan
#11/14/2023
#Lab10 Question3


try:
    num_file = open("numbers.txt", 'r')
    total = 0

except IOError:
    print("The file does not exist!")


for i in num_file :
    num = int(num_file.readline())
    
    if num < 100:
        total += num

print("The sum of the numbers from the file is", num)
        



    

    

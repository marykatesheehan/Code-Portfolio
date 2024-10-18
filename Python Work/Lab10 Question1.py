#Mary Kate Sheehan
#11/14/2023
#Lab10 Question1

def repeat(string, times):
    for i in range(times):
        print(string, end="")

def main():
    string = input("Enter something: ")
    times = int(input("Enter a positive number: "))
    repeat(string, times)

main()
    
